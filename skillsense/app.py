import os, sqlite3, hashlib, secrets
from flask import Flask, render_template, request, redirect, url_for, session, flash
from model import recommend

BASE = os.path.dirname(os.path.abspath(__file__))
DB   = os.path.join(BASE, "skillsense.db")
app  = Flask(__name__, template_folder=os.path.join(BASE,"templates"), static_folder=os.path.join(BASE,"static"))
app.secret_key = "skillsense-secret-key-2025"

def hash_pw(pw): return hashlib.sha256(pw.encode()).hexdigest()

def init_db():
    c = sqlite3.connect(DB)
    c.execute("""CREATE TABLE IF NOT EXISTS auth_accounts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        recovery_token TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP)""")
    c.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,email TEXT,qualification TEXT,skills TEXT,certifications TEXT,
        interests TEXT,programming_languages TEXT,subjects TEXT,created_at TEXT DEFAULT CURRENT_TIMESTAMP)""")
    c.execute("""CREATE TABLE IF NOT EXISTS recommendations(id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,skill TEXT,score REAL,rank_position INTEGER,career_paths TEXT,
        avg_salary TEXT,demand_level TEXT,explanation TEXT,created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id))""")
    c.commit(); c.close()

def save(f, recs):
    conn=sqlite3.connect(DB); c=conn.cursor()
    c.execute("INSERT INTO users(name,email,qualification,skills,certifications,interests,programming_languages,subjects) VALUES(?,?,?,?,?,?,?,?)",
        (f.get("name",""),f.get("email",""),f.get("qualification",""),f.get("skills",""),
         f.get("certifications",""),f.get("interests",""),f.get("programming_languages",""),f.get("subjects","")))
    uid=c.lastrowid
    for r in recs:
        c.execute("INSERT INTO recommendations(user_id,skill,score,rank_position,career_paths,avg_salary,demand_level,explanation) VALUES(?,?,?,?,?,?,?,?)",
            (uid,r["skill"],r["score"],r["rank"],r["career_paths"],str(r["avg_salary"]),r["demand_level"],r["explanation"]))
    conn.commit(); conn.close()

def get_history(n=15):
    conn=sqlite3.connect(DB); c=conn.cursor()
    c.execute("""SELECT u.name,u.qualification,r.skill,r.score,r.demand_level,r.created_at
        FROM recommendations r JOIN users u ON r.user_id=u.id
        WHERE r.rank_position=1 ORDER BY r.created_at DESC LIMIT ?""",(n,))
    rows=c.fetchall(); conn.close(); return rows

def get_stats():
    conn=sqlite3.connect(DB); c=conn.cursor()
    c.execute("SELECT COUNT(*) FROM users"); tu=c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM recommendations"); tr=c.fetchone()[0]
    c.execute("SELECT skill,COUNT(*) FROM recommendations GROUP BY skill ORDER BY COUNT(*) DESC LIMIT 1")
    top=c.fetchone(); conn.close()
    return {"total_users":tu,"total_recommendations":tr,"top_skill":top[0] if top else "N/A"}

def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

# ── AUTH ROUTES ──────────────────────────────────────────────────
@app.route("/login", methods=["GET","POST"])
def login():
    error_user = error_pass = None
    if request.method == "POST":
        uname = request.form.get("username","").strip()
        pw    = request.form.get("password","")
        conn  = sqlite3.connect(DB); c = conn.cursor()
        c.execute("SELECT password_hash FROM auth_accounts WHERE username=?", (uname,))
        row = c.fetchone(); conn.close()
        if row is None:
            error_user = "Username not found."
        elif row[0] != hash_pw(pw):
            error_pass = "Incorrect password."
        else:
            session["username"] = uname
            return redirect(url_for("index"))
    return render_template("login.html", error_user=error_user, error_pass=error_pass)

@app.route("/signup", methods=["GET","POST"])
def signup():
    error = None
    if request.method == "POST":
        uname = request.form.get("username","").strip()
        pw    = request.form.get("password","")
        pw2   = request.form.get("password2","")
        if not uname or not pw:
            error = "Username and password are required."
        elif len(uname) < 3:
            error = "Username must be at least 3 characters."
        elif len(pw) < 6:
            error = "Password must be at least 6 characters."
        elif pw != pw2:
            error = "Passwords do not match."
        else:
            try:
                conn = sqlite3.connect(DB); c = conn.cursor()
                c.execute("INSERT INTO auth_accounts(username,password_hash) VALUES(?,?)",(uname, hash_pw(pw)))
                conn.commit(); conn.close()
                session["username"] = uname
                return redirect(url_for("index"))
            except sqlite3.IntegrityError:
                error = "Username already taken. Please choose another."
    return render_template("signup.html", error=error)

@app.route("/forgot-password", methods=["GET","POST"])
def forgot_password():
    message = None; token_info = None
    if request.method == "POST":
        action = request.form.get("action","")
        if action == "request":
            uname = request.form.get("username","").strip()
            conn  = sqlite3.connect(DB); c = conn.cursor()
            c.execute("SELECT id FROM auth_accounts WHERE username=?", (uname,))
            row = c.fetchone()
            if row:
                token = secrets.token_hex(8)
                c.execute("UPDATE auth_accounts SET recovery_token=? WHERE username=?", (token, uname))
                conn.commit()
                token_info = {"username": uname, "token": token}
                message = "success"
            else:
                message = "not_found"
            conn.close()
        elif action == "reset":
            uname = request.form.get("username","").strip()
            token = request.form.get("token","").strip()
            new_pw = request.form.get("new_password","")
            new_pw2 = request.form.get("new_password2","")
            if new_pw != new_pw2:
                message = "mismatch"
            elif len(new_pw) < 6:
                message = "short"
            else:
                conn = sqlite3.connect(DB); c = conn.cursor()
                c.execute("SELECT id FROM auth_accounts WHERE username=? AND recovery_token=?", (uname, token))
                row = c.fetchone()
                if row:
                    c.execute("UPDATE auth_accounts SET password_hash=?, recovery_token=NULL WHERE username=?", (hash_pw(new_pw), uname))
                    conn.commit(); message = "reset_ok"
                else:
                    message = "bad_token"
                conn.close()
    return render_template("forgot_password.html", message=message, token_info=token_info)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ── MAIN ROUTES ──────────────────────────────────────────────────
@app.route("/")
@login_required
def index(): return render_template("index.html", username=session.get("username"))

@app.route("/recommend", methods=["POST"])
@login_required
def get_recs():
    f=request.form
    recs=recommend(qualification=f.get("qualification",""),skills=f.get("skills",""),
        certifications=f.get("certifications",""),interests=f.get("interests",""),
        programming_languages=f.get("programming_languages",""),subjects=f.get("subjects",""),top_n=5)
    if recs: save(f,recs)
    return render_template("result.html", recommendations=recs, form=f, username=session.get("username"))

@app.route("/history")
@login_required
def history(): return render_template("history.html", records=get_history(), stats=get_stats(), username=session.get("username"))

if __name__=="__main__":
    init_db()
    print("\n  SkillSense is running!  Open: http://127.0.0.1:5000\n")
    app.run(debug=True, port=5000)
