"""
setup_skillsense_v2.py  —  SkillSense Complete Setup (FIXED)
=============================================================
Run:   python setup_skillsense_v2.py
Opens: http://127.0.0.1:5000
"""

import os, sys, subprocess

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "skillsense")

def w(rel, content):
    path = os.path.join(BASE, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✔  {rel}")

# ══════════════════════════════════════════════════════════════
#  DATASET
# ══════════════════════════════════════════════════════════════
DATASET = """skill,qualifications,subjects,programming_languages,certifications,interests,description,career_paths,avg_salary,demand_level
Machine Learning,Bachelor in CS or Math or Statistics,Linear Algebra Calculus Statistics Data Structures Algorithms,Python R Julia,AWS ML Specialty Google ML Engineer TensorFlow Developer,AI Research Data Science Pattern Recognition Automation Prediction,Machine Learning involves building algorithms that learn from data to make predictions or decisions without being explicitly programmed. It combines mathematics statistics and programming to extract insights from complex datasets.,Data Scientist ML Engineer AI Researcher Research Scientist,120000,Very High
Web Development,Bachelor in CS or IT or any degree,HTML CSS JavaScript Algorithms Databases Networking,JavaScript TypeScript Python PHP Ruby,AWS Developer Meta Front-End Developer Google UX Design,Creative Design UI UX User Experience Web Applications Internet,Web Development is the craft of building and maintaining websites and web applications. It ranges from visual front-end design to server-side back-end logic covering everything users see and interact with online.,Frontend Developer Backend Developer Full-Stack Developer Web Designer,95000,Very High
Data Science,Bachelor in Statistics or CS or Economics or Mathematics,Statistics Probability Data Structures Linear Algebra Research Methods,Python R SQL Scala MATLAB,IBM Data Science Google Data Analytics Microsoft Azure Data,Data Analysis Visualization Business Intelligence Research Numbers,Data Science combines statistical analysis programming and domain expertise to extract actionable knowledge from structured and unstructured data.,Data Scientist Data Analyst Business Analyst Data Engineer,115000,Very High
Cybersecurity,Bachelor in CS or IT or Network Engineering,Networking Operating Systems Cryptography Algorithms Security,Python C C++ Bash Shell,CISSP CEH CompTIA Security+ OSCP,Network Security Ethical Hacking Privacy Digital Forensics Protection,Cybersecurity focuses on protecting computer systems networks and data from digital attacks theft and damage.,Security Analyst Penetration Tester SOC Analyst Security Engineer,110000,High
Cloud Computing,Bachelor in CS or IT or Engineering,Networking Distributed Systems Databases Operating Systems Architecture,Python Bash Shell Java Go,AWS Solutions Architect Azure Administrator Google Cloud Professional,Infrastructure Scalability DevOps Cloud Architecture Technology,Cloud Computing delivers computing services including servers storage databases networking software over the internet.,Cloud Architect DevOps Engineer Site Reliability Engineer Cloud Consultant,125000,Very High
Mobile App Development,Bachelor in CS or IT,Algorithms OOP Data Structures UI Design Mobile,Swift Kotlin Java Dart Flutter React Native,Google Associate Android Developer Apple iOS Development,App Design User Experience Mobile Technology Startups Innovation,Mobile App Development creates software applications that run on smartphones and tablets.,iOS Developer Android Developer Flutter Developer Mobile Architect,100000,High
Artificial Intelligence,Bachelor or Master in CS or Math,Logic Algorithms Linear Algebra Calculus Probability,Python Lisp Prolog C++,DeepMind AI Google AI IBM AI OpenAI,Research Robotics Cognitive Science Problem Solving Intelligence,Artificial Intelligence simulates human intelligence processes enabling machines to learn reason solve problems and plan.,AI Engineer NLP Engineer Computer Vision Engineer AI Researcher,130000,Very High
DevOps,Bachelor in CS or IT or Engineering,Networking Scripting Automation Systems Architecture,Python Bash Shell Ruby Go YAML,AWS DevOps Professional Docker Certified Kubernetes CKA,Automation Infrastructure Deployment CI CD Collaboration Systems,DevOps bridges software development and IT operations using automation tools to shorten development cycles.,DevOps Engineer Platform Engineer Release Manager Infrastructure Engineer,115000,High
Blockchain,Bachelor in CS or Finance or Engineering,Cryptography Distributed Systems Networking Economics Finance,Solidity JavaScript Python Go Rust,Certified Blockchain Developer Ethereum Developer,Finance Decentralization Cryptography Innovation Digital Currency,Blockchain is a distributed ledger technology recording transactions in tamper-resistant ways.,Blockchain Developer Smart Contract Engineer DeFi Developer Web3 Engineer,120000,Medium
Data Engineering,Bachelor in CS or Engineering or Math,Databases Distributed Systems Algorithms Data Structures ETL,Python SQL Scala Java Spark,Google Cloud Data Engineer AWS Data Analytics Databricks,Data Pipelines ETL Infrastructure Big Data Systems Architecture,Data Engineering builds infrastructure and pipelines that move transform and store large volumes of data.,Data Engineer Pipeline Engineer Big Data Engineer Analytics Engineer,118000,Very High
Full Stack Development,Bachelor in CS or IT or Self-taught,Databases Algorithms Networking UI Design APIs,JavaScript Python Node.js SQL React,Meta Full-Stack AWS Developer Full-Stack Web Bootcamp,Web Apps Startups APIs System Architecture Building,Full Stack Development encompasses both front-end and back-end development.,Full Stack Developer Technical Lead Software Engineer Startup CTO,105000,Very High
UI UX Design,Bachelor in Design or CS or Psychology or Fine Arts,Human-Computer Interaction Psychology Design Principles Color Theory,Figma Sketch HTML CSS Adobe XD,Google UX Design Nielsen Norman NN/g UX Certified,Design Creativity User Psychology Prototyping Aesthetics Art,UI/UX Design creates meaningful intuitive digital experiences by deeply understanding user needs behaviors and limitations.,UX Designer Product Designer UI Designer Design Systems Lead,95000,High
Game Development,Bachelor in CS or Game Design or Animation,Mathematics Physics Algorithms OOP Computer Graphics,C++ C# Unity UnrealScript Python,Unity Certified Developer Epic Games Unreal Certification,Gaming Storytelling Physics Simulation Creative Design Animation,Game Development combines programming art mathematics and storytelling to create interactive entertainment.,Game Developer Game Designer Technical Artist Engine Developer,90000,Medium
Digital Marketing,Bachelor in Marketing or Communications or Business or any field,Marketing Statistics Psychology Communications Consumer Behavior,Google Analytics SEO Tools Python SQL,Google Digital Marketing HubSpot Marketing Facebook Blueprint,Marketing Analytics Social Media Content Strategy Branding Advertising,Digital Marketing leverages online channels to connect brands with customers.,Digital Marketing Manager SEO Specialist Growth Hacker Performance Marketer,80000,High
Medicine and Healthcare,MBBS or Bachelor in Medicine or Nursing or Pharmacy,Biology Chemistry Anatomy Physiology Pathology Pharmacology,None,USMLE MBBS MD Nursing License Medical Certifications,Healthcare Patient Care Research Biology Science Helping Others Medicine,Medicine involves diagnosing treating and preventing illness and disease across hospitals clinics and research labs.,Doctor Surgeon Nurse Pharmacist Medical Researcher,100000,Very High
Clinical Psychology,Bachelor or Master in Psychology or Counseling,Psychology Human Behavior Mental Health Research Statistics Therapy,SPSS R,Licensed Psychologist Clinical Psychology Certification,Mental Health Counseling Behavior Research Human Mind Empathy Therapy,Clinical Psychology involves assessing diagnosing and treating mental emotional and behavioral disorders.,Clinical Psychologist Therapist Counselor Mental Health Specialist,85000,High
Law and Legal Studies,LLB or Bachelor in Law,Constitutional Law Criminal Law Civil Law Contract Law Jurisprudence,None,Bar Exam LLB LLM Advocate License,Justice Law Society Ethics Argumentation Policy Rights,Law involves advising clients on legal rights representing them in court and ensuring justice is served.,Lawyer Advocate Judge Legal Advisor Corporate Counsel,110000,High
Chartered Accountancy,Bachelor in Commerce or Accounting or Finance,Accounting Financial Management Taxation Auditing Economics,Tally SAP Excel,CA CPA CMA ACCA Chartered Accountant,Finance Numbers Taxation Auditing Accounting Business Commerce,Chartered Accountancy covers financial reporting auditing taxation and advisory services.,Chartered Accountant Auditor Tax Consultant Financial Advisor,95000,High
Finance and Investment Banking,Bachelor in Finance or Economics or Commerce or MBA,Economics Financial Markets Statistics Mathematics Portfolio Management,Excel Python Bloomberg SQL,CFA FRM Series 7 Investment Banking Certification,Finance Investment Markets Trading Economics Wealth Banking,Finance and Investment Banking involves managing capital assets investments and financial strategies for corporations.,Investment Banker Financial Analyst Portfolio Manager Risk Analyst,130000,Very High
Civil Engineering,Bachelor in Civil Engineering,Structural Analysis Fluid Mechanics Soil Mechanics Mathematics CAD,AutoCAD MATLAB Revit,Professional Engineer PE License PMP Construction Management,Construction Infrastructure Building Design Architecture Structures,Civil Engineering involves designing constructing and maintaining infrastructure including buildings roads bridges and dams.,Civil Engineer Structural Engineer Project Manager Site Engineer,85000,High
Mechanical Engineering,Bachelor in Mechanical Engineering,Thermodynamics Fluid Mechanics Mechanics of Materials Manufacturing Design,MATLAB AutoCAD SolidWorks,Professional Engineer PE License Six Sigma,Machines Design Manufacturing Automobiles Robotics Energy Mechanics,Mechanical Engineering applies physics and material science to design analyze and manufacture mechanical systems.,Mechanical Engineer Design Engineer Manufacturing Engineer,88000,High
Electrical Engineering,Bachelor in Electrical Engineering,Circuit Theory Electromagnetics Signal Processing Control Systems Power,MATLAB Python C,Professional Engineer PE License IEEE Certifications,Electronics Power Systems Circuits Signals Technology Energy,Electrical Engineering focuses on electricity electronics and electromagnetism designing power systems and electronic devices.,Electrical Engineer Electronics Engineer Power Engineer,90000,High
Architecture,Bachelor in Architecture or B.Arch,Architectural Design Structural Systems Urban Planning History of Architecture,AutoCAD Revit SketchUp,Licensed Architect RIBA Registration,Design Building Spaces Urban Planning Creativity Aesthetics Structures,Architecture combines art and science to design functional beautiful and sustainable buildings and spaces.,Architect Urban Planner Interior Designer Project Architect,80000,Medium
Interior Design,Bachelor in Interior Design or Fine Arts or Architecture,Design Principles Color Theory Space Planning Materials Decoration,AutoCAD SketchUp Revit Adobe Creative Suite,NCIDQ Interior Design Certification,Design Creativity Aesthetics Space Decoration Art Homes,Interior Design creates functional aesthetically pleasing indoor environments combining creativity with knowledge of materials.,Interior Designer Space Planner Furniture Designer Set Designer,65000,Medium
Fashion Design,Bachelor in Fashion Design or Textile Technology,Fashion History Textile Science Pattern Making Illustration Clothing,Adobe Illustrator Photoshop,Fashion Design Certification Textile Technology,Fashion Creativity Art Clothing Style Trends Culture Beauty,Fashion Design involves creating clothing accessories and footwear combining artistic creativity with knowledge of textiles.,Fashion Designer Textile Designer Stylist Fashion Buyer,60000,Medium
Journalism and Mass Communication,Bachelor in Journalism or Mass Communication or English,Media Studies Writing Communication Ethics Political Science Reporting,None,Press Club Certification Reuters Journalism,Writing Media News Storytelling Current Affairs Communication Society,Journalism investigates and reports on events issues and trends informing the public through newspapers television and digital media.,Journalist Reporter Editor News Anchor Content Writer,65000,Medium
Content Writing and Copywriting,Bachelor in English or Journalism or any degree,English Literature Writing Grammar Communication Marketing,None,HubSpot Content Marketing Google Digital Marketing,Writing Creativity Language Storytelling Marketing Communication Blogging,Content Writing and Copywriting involves creating compelling written material for websites blogs social media and advertisements.,Content Writer Copywriter SEO Writer Technical Writer,70000,High
Teaching and Education,Bachelor in Education or B.Ed or any subject degree,Pedagogy Psychology Child Development Subject Knowledge Curriculum,None,B.Ed Teaching License TET CTET,Teaching Children Education Knowledge Sharing Mentoring Learning,Teaching involves educating students at various levels from primary school to university imparting knowledge skills and values.,Teacher Professor Lecturer Academic Counselor,55000,High
Human Resources Management,Bachelor in HR or Business Administration or Psychology,Organizational Behavior Human Psychology Management Labor Law Recruitment,SAP HR Excel,SHRM PHR SPHR HR Certification,People Management Recruitment Training Employee Relations Organizations,Human Resources Management involves recruiting developing and retaining talent managing employee relations.,HR Manager Recruiter Training Manager Talent Acquisition Specialist,75000,High
Supply Chain and Logistics,Bachelor in Logistics or Business or Engineering,Operations Research Supply Chain Management Statistics Economics,SAP Oracle Excel,CSCP CLTD Six Sigma Green Belt,Logistics Operations Management Trade Transportation Planning,Supply Chain Management oversees the flow of goods services information and finances from origin to consumer.,Supply Chain Manager Logistics Coordinator Operations Manager Procurement Specialist,80000,High
Hospitality and Hotel Management,Bachelor in Hotel Management or Tourism or Business,Food Science Hospitality Management Tourism Marketing Service,PMS Hotel Software,Hotel Management Certification FSSAI Food Safety,Hospitality Travel Tourism Food Service People Customers,Hospitality Management involves managing hotels restaurants resorts and tourism services.,Hotel Manager Restaurant Manager Event Manager Travel Consultant,60000,Medium
Event Management,Bachelor in Event Management or Mass Communication or Business,Event Planning Marketing Communication Public Relations Management,None,Event Management Certification CSEP,Events Planning Creativity Coordination People Networking Social,Event Management involves planning organizing and executing events from corporate conferences to weddings and concerts.,Event Manager Wedding Planner Conference Coordinator PR Manager,65000,Medium
Graphic Design,Bachelor in Graphic Design or Fine Arts or Visual Communication,Design Principles Typography Color Theory Visual Arts Branding,Adobe Photoshop Illustrator InDesign Figma,Adobe Certified Expert Canva Design Certification,Design Creativity Art Visual Communication Branding Advertising,Graphic Design uses visual elements typography and imagery to communicate ideas and messages for branding and advertising.,Graphic Designer Brand Designer Visual Designer Art Director,70000,High
Photography and Videography,Bachelor in Fine Arts or Mass Communication or any degree,Photography Visual Arts Composition Lighting Film Studies,Adobe Lightroom Premiere Pro Photoshop,Photography Certification Adobe Certified,Photography Art Storytelling Visual Media Creativity Film,Photography and Videography capture visual stories through still images and moving pictures for journalism and entertainment.,Photographer Videographer Cinematographer Photo Editor,60000,Medium
Social Work,Bachelor in Social Work or Sociology or Psychology,Sociology Psychology Social Policy Community Development Welfare,SPSS,Licensed Social Worker MSW Certification,Helping Others Community Service Human Rights Welfare NGO,Social Work involves supporting individuals families and communities facing challenges to improve their wellbeing.,Social Worker Community Worker NGO Manager Child Welfare Officer,50000,Medium
Environmental Science,Bachelor in Environmental Science or Biology or Chemistry,Ecology Biology Chemistry Earth Science Environmental Policy,R Python MATLAB,LEED Green Associate Environmental Science Certification,Environment Nature Conservation Sustainability Research Climate,Environmental Science studies the interaction between humans and the natural world addressing challenges like climate change.,Environmental Scientist Conservation Officer Environmental Consultant,75000,High
Biotechnology,Bachelor in Biotechnology or Biology or Chemistry,Molecular Biology Genetics Biochemistry Microbiology Lab Science,Python R MATLAB Bioinformatics tools,Biotechnology Certification Bioinformatics GMP,Biology Research Science Healthcare Innovation Lab Work Genetics,Biotechnology applies biological systems to develop new products and technologies in medicine agriculture and food production.,Biotechnologist Research Scientist Biomedical Engineer Lab Analyst,85000,High
Pharmacy,Bachelor in Pharmacy or B.Pharm,Pharmacology Medicinal Chemistry Pharmaceutical Analysis Physiology,None,Pharmacist License B.Pharm D.Pharm,Medicine Chemistry Healthcare Drug Research Patient Care,Pharmacy involves preparing dispensing and advising on medications ensuring safe and effective drug use.,Pharmacist Drug Researcher Clinical Pharmacist Hospital Pharmacist,80000,High
Nutrition and Dietetics,Bachelor in Nutrition or Dietetics or Food Science,Nutrition Science Biochemistry Physiology Food Science Health,None,Registered Dietitian RD Nutrition Certification,Health Food Wellness Diet Fitness Science Biology,Nutrition and Dietetics studies how food affects health helping individuals manage diseases and maintain health through dietary guidance.,Dietitian Nutritionist Public Health Nutritionist Sports Nutritionist,65000,Medium
Sports Science and Fitness,Bachelor in Sports Science or Physical Education or Kinesiology,Exercise Physiology Biomechanics Anatomy Sports Psychology Fitness,None,Personal Training CPT Sports Coaching Certification,Sports Fitness Health Exercise Coaching Athletics Wellness,Sports Science applies scientific principles to improve athletic performance prevent injury and promote physical fitness.,Sports Scientist Fitness Coach Athletic Trainer Physical Education Teacher,60000,Medium
Animation and VFX,Bachelor in Animation or Fine Arts or CS,2D 3D Animation Visual Effects Storytelling Design,Maya Blender After Effects Nuke,Autodesk Certified Maya VFX Certification,Animation Movies Games Art Storytelling Creativity Film,Animation and Visual Effects create moving images for films television video games and digital media.,Animator VFX Artist Motion Graphics Designer 3D Artist,75000,High
Music Production,Bachelor in Music or Fine Arts or Audio Engineering,Music Theory Composition Sound Design Audio Engineering,Ableton Logic Pro FL Studio,Music Production Certification Berklee Online,Music Audio Creativity Sound Art Performance Entertainment,Music Production involves composing arranging recording mixing and mastering music for albums film and digital platforms.,Music Producer Sound Engineer Composer Music Arranger,70000,Medium
Public Administration,Bachelor in Public Administration or Political Science or Law,Public Policy Governance Economics Constitutional Law Ethics Management,SPSS,IAS IPS Government Services Civil Services Examination,Governance Policy Public Service Leadership Nation Building Administration,Public Administration involves managing government agencies implementing public policies and delivering services to citizens.,IAS Officer Civil Servant Policy Analyst Government Manager,70000,High
Entrepreneurship,Bachelor in Business or Engineering or any field,Business Management Marketing Finance Strategy Leadership Innovation,Excel Python,MBA Startup Incubation Entrepreneurship Certification,Business Innovation Startups Leadership Risk-Taking Creativity Ventures,Entrepreneurship involves identifying opportunities creating new businesses and managing ventures to deliver value.,Entrepreneur Startup Founder Business Owner Venture Capitalist,Variable,High
Real Estate,Bachelor in Business or Civil Engineering or Finance,Real Estate Law Economics Finance Market Analysis Property,Excel,Real Estate License RERA Certification,Property Investment Land Buildings Finance Market Architecture,Real Estate involves buying selling renting and managing properties including residential commercial and industrial assets.,Real Estate Agent Property Manager Real Estate Analyst Land Developer,75000,Medium
Forensic Science,Bachelor in Forensic Science or Chemistry or Biology,Chemistry Biology Criminalistics Toxicology Evidence Analysis,None,Forensic Science Certification Crime Scene Investigation,Crime Science Investigation Justice Lab Research Mysteries,Forensic Science applies scientific methods to criminal investigations analyzing physical evidence to support legal proceedings.,Forensic Scientist Crime Scene Investigator Forensic Analyst Toxicologist,70000,Medium
Veterinary Science,Bachelor in Veterinary Science or BVSc,Animal Anatomy Physiology Pharmacology Pathology Biology,None,Veterinary License BVSc,Animals Biology Nature Healthcare Science Wildlife,Veterinary Science diagnoses treats and prevents diseases in animals ranging from pets and livestock to wildlife.,Veterinarian Animal Health Officer Wildlife Biologist,75000,Medium
Economics,Bachelor in Economics or Commerce or Statistics,Microeconomics Macroeconomics Econometrics Statistics Mathematics Finance,Python R Stata SPSS,CFA Economics Certification,Economics Finance Policy Research Analysis Markets Trade,Economics studies how individuals businesses and governments allocate scarce resources analyzing markets and predicting trends.,Economist Policy Analyst Financial Analyst Market Research Analyst,90000,High
Political Science and International Relations,Bachelor in Political Science or International Relations or Law,Political Theory International Law Diplomacy Public Policy History,None,Foreign Service Examination Diplomatic Training,Politics Governance Global Affairs Policy Diplomacy Leadership,Political Science and International Relations study political systems governance diplomacy and global affairs.,Political Analyst Diplomat Foreign Service Officer Policy Advisor,75000,Medium
Sociology and Anthropology,Bachelor in Sociology or Anthropology or Social Sciences,Social Theory Research Methods Cultural Studies Statistics,SPSS R,Research Certification,Society Culture Human Behavior Community Research Social Sciences,Sociology and Anthropology study human societies cultures behaviors and social structures.,Sociologist Anthropologist Social Researcher Community Developer,65000,Low
Fine Arts and Painting,Bachelor in Fine Arts or Visual Arts,Drawing Painting Sculpture Art History Color Theory,Adobe Photoshop Illustrator,Fine Arts Degree Art Exhibition,Art Creativity Painting Expression Culture Visual,Fine Arts and Painting involves creating visual art through drawing painting sculpture and mixed media.,Artist Painter Sculptor Art Teacher Gallery Curator,55000,Low
Theatre and Performing Arts,Bachelor in Theatre or Performing Arts or Drama,Acting Directing Script Writing Theatre History Voice Performance,None,Theatre Arts Degree Drama Certification,Acting Performance Storytelling Theatre Drama Creativity Entertainment,Theatre and Performing Arts involve acting directing writing and producing live performances on stage.,Actor Director Stage Manager Theatre Educator,55000,Low
Food Technology,Bachelor in Food Technology or Food Science or Chemistry,Food Science Microbiology Chemistry Nutrition Food Processing,None,FSSAI Food Safety Certification,Food Science Technology Processing Quality Safety,Food Technology applies science to the processing preservation packaging and quality control of food products.,Food Technologist Quality Control Manager Food Safety Auditor,70000,Medium
Agricultural Science,Bachelor in Agriculture or Agricultural Science,Agronomy Soil Science Plant Biology Animal Science Economics Farming,None,Agriculture Certification Agri Business,Farming Agriculture Nature Food Production Sustainability Environment,Agricultural Science studies crop production soil science animal husbandry and agricultural economics.,Agricultural Scientist Farm Manager Agronomist Agricultural Officer,65000,Medium
Physiotherapy,Bachelor in Physiotherapy or BPT,Anatomy Physiology Kinesiology Rehabilitation Science Exercise,None,BPT Physiotherapy License Sports Medicine,Health Rehabilitation Movement Fitness Healing Body,Physiotherapy rehabilitates patients with physical injuries using exercise manual therapy and physical interventions.,Physiotherapist Sports Therapist Rehabilitation Specialist,70000,High
Dental Science,Bachelor in Dentistry or BDS,Oral Anatomy Dental Materials Pathology Pharmacology Surgery,None,BDS MDS Dentist License,Healthcare Teeth Science Medicine Patient Care Oral Health,Dental Science focuses on oral health diagnosing treating and preventing diseases of the teeth gums and mouth.,Dentist Orthodontist Oral Surgeon Dental Researcher,95000,High
Renewable Energy,Bachelor in Electrical or Mechanical or Environmental Engineering,Energy Systems Power Electronics Thermodynamics Renewable Technology,MATLAB Python,Renewable Energy Certification Solar Panel Installation,Energy Sustainability Environment Solar Wind Technology Green,Renewable Energy focuses on harnessing solar wind hydro geothermal and biomass energy to replace fossil fuels.,Solar Engineer Wind Energy Specialist Energy Consultant Renewable Project Manager,90000,High
Project Management,Bachelor in any Engineering or Business or CS,Project Planning Risk Management Resource Allocation Leadership Scheduling,MS Project JIRA Excel,PMP PRINCE2 Agile Scrum,Planning Organizing Leadership Execution Coordination Management,Project Management involves planning organizing and overseeing projects to achieve specific goals within time budget and quality constraints.,Project Manager Program Manager Scrum Master Agile Coach,95000,Very High
Operations Management,Bachelor in Business or Engineering or Operations,Operations Research Supply Chain Quality Management Process Improvement,SAP ERP Excel,Six Sigma PMP Operations Management Certification,Operations Efficiency Management Process Optimization Business,Operations Management optimizes business processes production and service delivery to maximize efficiency quality and profitability.,Operations Manager Production Manager Process Improvement Manager,85000,High
Sales and Business Development,Bachelor in Business or Marketing or any field,Sales Marketing Communication Psychology Negotiation Customer Relations,CRM Software Excel,Sales Certification Salesforce,Sales Business Networking Communication Persuasion Revenue,Sales and Business Development involves identifying new business opportunities building client relationships and growing revenue.,Sales Manager Business Development Manager Account Executive,85000,Very High
Insurance and Actuarial Science,Bachelor in Mathematics or Statistics or Commerce,Actuarial Science Probability Statistics Finance Risk Management,Excel Python R,Actuarial Certification CA Insurance License,Risk Mathematics Finance Insurance Analysis Numbers,Actuarial Science applies mathematics and statistics to assess financial risk in insurance pensions and investments.,Actuary Risk Analyst Insurance Underwriter Pension Consultant,105000,High
Aeronautical Engineering,Bachelor in Aeronautical Engineering or Aerospace Engineering,Aerodynamics Thermodynamics Structural Analysis Propulsion Mathematics,MATLAB Python AutoCAD,Aeronautical Engineering Certification,Aviation Aircraft Flight Engineering Technology Science,Aeronautical Engineering designs develops and tests aircraft systems ensuring airworthiness performance and safety standards.,Aeronautical Engineer Flight Test Engineer Aircraft Designer Aerospace Analyst,100000,Medium
Aviation and Pilot Training,Bachelor in Aviation or any degree,Physics Mathematics Aviation Science Navigation Meteorology,Flight Simulator Software,Commercial Pilot License CPL ATPL,Flying Aviation Travel Adventure Technology Aircraft,Aviation involves piloting aircraft navigating airspace and managing flight operations across commercial military and cargo sectors.,Commercial Pilot Flight Instructor Air Traffic Controller Aviation Manager,120000,High
Culinary Arts,Diploma in Culinary Arts or Hotel Management,Food Science Nutrition Culinary Techniques Kitchen Management,None,Chef Certification Culinary Arts Diploma,Cooking Food Creativity Hospitality Culture Travel Cuisine,Culinary Arts involves professional cooking food preparation menu design and kitchen management.,Chef Head Chef Pastry Chef Food Stylist,60000,Medium
Sports Management,Bachelor in Sports Management or Business or Physical Education,Sports Marketing Management Finance Event Management Leadership,Excel,Sports Management Certification,Sports Business Management Events Organization Team,Sports Management involves the business and administrative aspects of sport including team management and marketing.,Sports Manager Club Administrator Sports Marketing Manager Event Coordinator,70000,Medium
"""

# ══════════════════════════════════════════════════════════════
#  MODEL.PY
# ══════════════════════════════════════════════════════════════
MODEL_PY = '''import os, pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.DataFrame(); tfidf = TfidfVectorizer(); skill_vectors = None

def load():
    global df, tfidf, skill_vectors
    df = pd.read_csv(os.path.join(BASE_DIR, "dataset.csv"))
    df["combined"] = (
        df["qualifications"].fillna("")+" "+df["qualifications"].fillna("")+" "+
        df["subjects"].fillna("")+" "+df["subjects"].fillna("")+" "+
        df["programming_languages"].fillna("")+" "+df["certifications"].fillna("")+" "+
        df["interests"].fillna("")+" "+df["interests"].fillna("")+" "+
        df["description"].fillna("")+" "+df["career_paths"].fillna("")
    )
    tfidf = TfidfVectorizer(stop_words="english", ngram_range=(1,2), max_features=8000, sublinear_tf=True)
    skill_vectors = tfidf.fit_transform(df["combined"])
    print(f"[Model] {len(df)} skills loaded")

def _ov(a, b):
    if not a or not b: return []
    return [w.capitalize() for w in set(a.lower().replace(","," ").split()) & set(b.lower().replace(","," ").split()) if len(w)>2][:4]

def _explain(skill, score, qual, langs, interests, subjects, certs, row):
    p = []
    if score>=70: p.append(f"Based on a strong compatibility score of {score}%, {skill} stands out as an excellent match for your profile.")
    elif score>=40: p.append(f"With a compatibility score of {score}%, {skill} is a well-suited choice aligned with your background.")
    else: p.append(f"{skill} has been identified as a potential growth direction with a compatibility score of {score}%.")
    if qual:
        m=_ov(qual,row["qualifications"])
        p.append(f"Your educational background in {qual} directly aligns with the qualifications required for {skill}" + (f", especially in {', '.join(m)}." if m else "."))
    if subjects:
        m=_ov(subjects,row["subjects"])
        if m: p.append(f"Your knowledge of {', '.join(m)} is directly relevant to the academic demands of {skill}.")
    if langs and row["programming_languages"].strip().lower() not in ["none",""]:
        m=_ov(langs,row["programming_languages"])
        if m: p.append(f"Your proficiency in {', '.join(m)} gives you a head start in {skill}.")
    if interests:
        m=_ov(interests,row["interests"])
        if m: p.append(f"Your passion for {', '.join(m)} strongly aligns with the work in {skill}.")
    if certs and certs.strip().lower() not in ["none",""]:
        m=_ov(certs,row["certifications"])
        if m: p.append(f"Your certification(s) in {', '.join(m)} are recognised credentials in the {skill} domain.")
    sal = row["avg_salary"]
    sal_str = f"~${int(sal)//1000}K/yr" if str(sal).lower()!="variable" else "variable (based on business success)"
    p.append(f"Career-wise, {skill} opens doors to: {row[\'career_paths\']}. Average salary: {sal_str} with {row[\'demand_level\'].lower()} market demand.")
    return " ".join(p)

def recommend(qualification="", skills="", certifications="", interests="", programming_languages="", subjects="", top_n=5):
    global df, skill_vectors
    if df.empty or skill_vectors is None: load()
    user = " ".join(filter(None,[qualification,qualification,subjects,subjects,interests,interests,skills,certifications,programming_languages]))
    if not user.strip(): return []
    sims = cosine_similarity(tfidf.transform([user]), skill_vectors).flatten()
    results=[]
    for rank,idx in enumerate(sims.argsort()[::-1][:top_n]):
        row=df.iloc[idx]; score=round(float(sims[idx])*100,1)
        results.append({"rank":rank+1,"skill":row["skill"],"score":score,"description":row["description"],
            "career_paths":row["career_paths"],"avg_salary":row["avg_salary"],"demand_level":row["demand_level"],
            "explanation":_explain(row["skill"],score,qualification,programming_languages,interests,subjects,certifications,row)})
    return results

load()
'''

# ══════════════════════════════════════════════════════════════
#  APP.PY
# ══════════════════════════════════════════════════════════════
APP_PY = '''import os, sqlite3, hashlib, secrets
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
    print("\\n  SkillSense is running!  Open: http://127.0.0.1:5000\\n")
    app.run(debug=True, port=5000)
'''

# ══════════════════════════════════════════════════════════════
#  INDEX.HTML
# ══════════════════════════════════════════════════════════════
INDEX_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>SkillSense — AI Skill Recommender</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}"/>
</head>
<body>

<nav class="nav">
  <div class="nav-inner">
    <a class="logo" href="/">Skill<span>Sense</span></a>
    <div class="nav-links">
      <a href="/">Home</a>
      <a href="/history">History</a>
      <span class="nav-user">👤 {{ username }}</span>
      <a href="/logout" class="nav-logout">Sign Out</a>
    </div>
  </div>
</nav>

<header class="hero">
  <div class="hero-bg">
    <div class="blob b1"></div>
    <div class="blob b2"></div>
    <div class="grid-overlay"></div>
  </div>
  <div class="hero-content">
    <div class="badge">✦ ML-Powered &middot; TF-IDF + Cosine Similarity</div>
    <h1>Discover Your<br/><span class="gradient-text">Perfect Skill Path</span></h1>
    <p class="hero-sub">Enter your background and let our AI engine map your unique strengths to the highest-impact career skills — across every field.</p>
    <a href="#form-section" class="cta-btn" id="startBtn">
      Start Analysis
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
    </a>
  </div>
  <div class="floating-cards">
    <div class="fc fc1"><span>🤖</span><span>Machine Learning</span></div>
    <div class="fc fc2"><span>⚖️</span><span>Law &amp; Legal Studies</span></div>
    <div class="fc fc3"><span>🏥</span><span>Medicine &amp; Healthcare</span></div>
    <div class="fc fc4"><span>💰</span><span>Finance &amp; Banking</span></div>
  </div>
</header>

<section class="how-section">
  <div class="container">
    <div class="section-label">How It Works</div>
    <h2 class="section-title">Three Steps to Clarity</h2>
    <div class="steps">
      <div class="step">
        <div class="step-num">01</div>
        <div class="step-body"><h3>Enter Your Profile</h3><p>Share your qualification, skills, interests, and programming knowledge — any field, any background.</p></div>
      </div>
      <div class="step-arrow">&#8594;</div>
      <div class="step">
        <div class="step-num">02</div>
        <div class="step-body"><h3>ML Analysis</h3><p>TF-IDF vectorises your profile and cosine similarity scores it against 65+ career paths across all industries.</p></div>
      </div>
      <div class="step-arrow">&#8594;</div>
      <div class="step">
        <div class="step-num">03</div>
        <div class="step-body"><h3>Get Results</h3><p>Receive personalised top-5 skills with AI-generated explanations, salaries, and career paths.</p></div>
      </div>
    </div>
  </div>
</section>

<section id="form-section" class="form-section">
  <div class="container">
    <div class="form-wrap">
      <div class="form-header">
        <div class="section-label">Your Profile</div>
        <h2 class="section-title">Tell Us About Yourself</h2>
        <p>Fill in as many fields as possible for the most accurate recommendations. Works for every field — tech, medicine, law, arts, business and more.</p>
      </div>
      <form action="/recommend" method="POST" class="skill-form" id="skillForm">
        <div class="form-row two-col">
          <div class="field-group">
            <label for="name">&#128100; Full Name</label>
            <input type="text" id="name" name="name" placeholder="e.g. Priya Sharma" required/>
          </div>
          <div class="field-group">
            <label for="email">&#9993; Email</label>
            <input type="email" id="email" name="email" placeholder="e.g. priya@email.com"/>
          </div>
        </div>
        <div class="form-row">
          <div class="field-group">
            <label for="qualification">&#127891; Qualification / Degree</label>
            <input type="text" id="qualification" name="qualification" placeholder="e.g. MBBS, LLB, B.Tech CS, B.Com, BFA, B.Arch"/>
          </div>
        </div>
        <div class="form-row two-col">
          <div class="field-group">
            <label for="subjects">&#128218; Subjects Known</label>
            <input type="text" id="subjects" name="subjects" placeholder="e.g. Anatomy, Calculus, Law, Accounting, Drawing"/>
            <small>Comma-separated</small>
          </div>
          <div class="field-group">
            <label for="programming_languages">&#128187; Programming Languages</label>
            <input type="text" id="programming_languages" name="programming_languages" placeholder="e.g. Python, Java, C++ (or leave blank)"/>
            <small>Comma-separated</small>
          </div>
        </div>
        <div class="form-row">
          <div class="field-group">
            <label for="skills">&#11088; Current Skills</label>
            <input type="text" id="skills" name="skills" placeholder="e.g. Patient Care, Legal Drafting, Painting, SQL, Teaching"/>
            <small>Comma-separated</small>
          </div>
        </div>
        <div class="form-row two-col">
          <div class="field-group">
            <label for="certifications">&#127941; Certifications</label>
            <input type="text" id="certifications" name="certifications" placeholder="e.g. CA, MBBS License, AWS, Bar Exam (or leave blank)"/>
            <small>Comma-separated</small>
          </div>
          <div class="field-group">
            <label for="interests">&#10084; Areas of Interest</label>
            <input type="text" id="interests" name="interests" placeholder="e.g. Healthcare, Justice, Finance, Art, Technology"/>
            <small>Comma-separated</small>
          </div>
        </div>
        <div class="form-submit">
          <button type="submit" class="submit-btn" id="submitBtn">
            <span class="btn-text">Analyse My Profile &#8594;</span>
            <span class="btn-loader" style="display:none">Analysing&#8230;</span>
          </button>
        </div>
      </form>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="container">
    <div class="footer-inner">
      <span class="logo">Skill<span>Sense</span></span>
      <span class="footer-note">Built with Python &middot; Flask &middot; TF-IDF &middot; SQLite &middot; 65+ Skills</span>
    </div>
  </div>
</footer>

<script>
document.getElementById("startBtn").addEventListener("click",function(e){
  e.preventDefault();
  document.getElementById("form-section").scrollIntoView({behavior:"smooth"});
});
document.getElementById("skillForm").addEventListener("submit",function(){
  var btn=document.getElementById("submitBtn");
  btn.querySelector(".btn-text").style.display="none";
  btn.querySelector(".btn-loader").style.display="inline";
  btn.disabled=true;
});
</script>
</body>
</html>
"""

# ══════════════════════════════════════════════════════════════
#  RESULT.HTML
# ══════════════════════════════════════════════════════════════
RESULT_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Your Results &mdash; SkillSense</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}"/>
</head>
<body class="result-page">
<nav class="nav">
  <div class="nav-inner">
    <a class="logo" href="/">Skill<span>Sense</span></a>
    <div class="nav-links"><a href="/">Home</a><a href="/history">History</a><span class="nav-user">👤 {{ username }}</span><a href="/logout" class="nav-logout">Sign Out</a></div>  </div>
</nav>

<section class="result-hero">
  <div class="rh-bg"><div class="blob b1"></div><div class="blob b3"></div></div>
  <div class="container">
    <div class="badge">&#10022; Analysis Complete</div>
    <h1>Hello, <span class="gradient-text">{{ form.get('name', 'there') }}</span>!</h1>
    <p class="hero-sub">Our ML engine found <strong>{{ recommendations|length }}</strong> personalised skill recommendations for you.</p>
  </div>
</section>

{% if recommendations %}
{% set top = recommendations[0] %}
<section class="top-pick-section">
  <div class="container">
    <div class="top-pick-card">
      <div class="tp-left">
        <div class="tp-label">&#127942; Best Match &mdash; Rank #1</div>
        <h2 class="tp-skill">{{ top.skill }}</h2>
        <div class="tp-score-bar-wrap">
          <div class="tp-score-label">Compatibility Score</div>
          <div class="tp-bar-track"><div class="tp-bar-fill" id="topBar" style="width:0%"></div></div>
          <div class="tp-score-num">{{ top.score }}%</div>
        </div>
        <div class="tp-tags">
          <span class="tag tag-demand">{{ top.demand_level }} Demand</span>
          <span class="tag tag-salary">
            {% if top.avg_salary == 'Variable' or top.avg_salary == 'variable' %}
              Variable Salary
            {% else %}
              Avg. ${{ '{:,}'.format(top.avg_salary|int) }}/yr
            {% endif %}
          </span>
        </div>
      </div>
      <div class="tp-right">
        <div class="tp-section-label">Why This Skill?</div>
        <p class="tp-explanation">{{ top.explanation }}</p>
        <div class="tp-careers-label">Career Paths</div>
        <div class="tp-careers">
          {% for c in top.career_paths.split(',') %}
            <span class="career-chip">{{ c.strip() }}</span>
          {% endfor %}
        </div>
      </div>
    </div>
  </div>
</section>

<section class="recs-section">
  <div class="container">
    <div class="section-label">All Recommendations</div>
    <h2 class="section-title">Your Top 5 Skill Paths</h2>
    <div class="recs-grid">
      {% for rec in recommendations %}
      <div class="rec-card {% if rec.rank == 1 %}rec-card--top{% endif %}" style="animation-delay:{{ loop.index0 * 0.08 }}s">
        <div class="rc-header">
          <div class="rc-rank">#{{ rec.rank }}</div>
          <div class="rc-skill">{{ rec.skill }}</div>
          <div class="rc-score">{{ rec.score }}%</div>
        </div>
        <div class="rc-bar-track"><div class="rc-bar-fill" style="width:0%" data-w="{{ rec.score }}"></div></div>
        <p class="rc-desc">{{ rec.description[:155] }}...</p>
        <div class="rc-meta">
          <div class="rc-meta-item">&#128176;
            {% if rec.avg_salary == 'Variable' or rec.avg_salary == 'variable' %}
              Variable
            {% else %}
              ${{ '{:,}'.format(rec.avg_salary|int) }}/yr
            {% endif %}
          </div>
          <div class="rc-meta-item">&#128200; {{ rec.demand_level }}</div>
        </div>
        <details class="rc-expand">
          <summary>Why this recommendation?</summary>
          <p class="rc-explanation">{{ rec.explanation }}</p>
          <div class="rc-careers">
            {% for c in rec.career_paths.split(',') %}<span class="career-chip">{{ c.strip() }}</span>{% endfor %}
          </div>
        </details>
      </div>
      {% endfor %}
    </div>
  </div>
</section>
{% else %}
<section class="container" style="padding:5rem 1rem;text-align:center">
  <h2>No recommendations found.</h2>
  <p style="margin-top:1rem;color:#6b7a99">Please go back and fill in more profile details.</p>
  <a href="/" class="cta-btn" style="margin-top:2rem;display:inline-flex">&#8592; Try Again</a>
</section>
{% endif %}

<section class="profile-summary-section">
  <div class="container">
    <div class="ps-card">
      <div class="section-label">Profile Used</div>
      <h3>Your Input Summary</h3>
      <div class="ps-grid">
        {% if form.get('qualification') %}<div class="ps-item"><span class="ps-key">Qualification</span><span class="ps-val">{{ form.get('qualification') }}</span></div>{% endif %}
        {% if form.get('programming_languages') %}<div class="ps-item"><span class="ps-key">Languages</span><span class="ps-val">{{ form.get('programming_languages') }}</span></div>{% endif %}
        {% if form.get('skills') %}<div class="ps-item"><span class="ps-key">Skills</span><span class="ps-val">{{ form.get('skills') }}</span></div>{% endif %}
        {% if form.get('subjects') %}<div class="ps-item"><span class="ps-key">Subjects</span><span class="ps-val">{{ form.get('subjects') }}</span></div>{% endif %}
        {% if form.get('certifications') %}<div class="ps-item"><span class="ps-key">Certifications</span><span class="ps-val">{{ form.get('certifications') }}</span></div>{% endif %}
        {% if form.get('interests') %}<div class="ps-item"><span class="ps-key">Interests</span><span class="ps-val">{{ form.get('interests') }}</span></div>{% endif %}
      </div>
      <a href="/" class="cta-btn" style="margin-top:2rem;display:inline-flex">&#8592; Try Another Profile</a>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="container">
    <div class="footer-inner">
      <span class="logo">Skill<span>Sense</span></span>
      <span class="footer-note">Built with Python &middot; Flask &middot; TF-IDF &middot; SQLite</span>
    </div>
  </div>
</footer>

<script>
window.addEventListener("load", function(){
  var topBar = document.getElementById("topBar");
  if(topBar){ setTimeout(function(){ topBar.style.width = "{{ top.score if recommendations else 0 }}%"; topBar.style.transition = "width 1.4s cubic-bezier(0.22,1,0.36,1)"; }, 200); }
  document.querySelectorAll(".rc-bar-fill").forEach(function(el){
    var w = el.getAttribute("data-w");
    setTimeout(function(){ el.style.width = w + "%"; el.style.transition = "width 1s ease"; }, 400);
  });
});
</script>
</body>
</html>
"""

# ══════════════════════════════════════════════════════════════
#  HISTORY.HTML
# ══════════════════════════════════════════════════════════════
HISTORY_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>History &mdash; SkillSense</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}"/>
</head>
<body>
<nav class="nav">
  <div class="nav-inner">
    <a class="logo" href="/">Skill<span>Sense</span></a>
    <div class="nav-links"><a href="/">Home</a><a href="/history" class="active">History</a><span class="nav-user">👤 {{ username }}</span><a href="/logout" class="nav-logout">Sign Out</a></div>
  </div>
</nav>

<section class="result-hero" style="padding:7rem 0 3rem">
  <div class="rh-bg"><div class="blob b2"></div></div>
  <div class="container">
    <div class="badge">&#10022; SQLite Database</div>
    <h1>Recommendation <span class="gradient-text">History</span></h1>
    <p class="hero-sub">All past analyses stored securely in your local database.</p>
  </div>
</section>

<section class="history-section">
  <div class="container">
    <div class="stats-row">
      <div class="stat-card">
        <div class="stat-num">{{ stats.total_users }}</div>
        <div class="stat-label">Total Users</div>
      </div>
      <div class="stat-card">
        <div class="stat-num">{{ stats.total_recommendations }}</div>
        <div class="stat-label">Total Recommendations</div>
      </div>
      <div class="stat-card">
        <div class="stat-num" style="font-size:1.3rem;padding-top:0.4rem">{{ stats.top_skill }}</div>
        <div class="stat-label">Most Recommended</div>
      </div>
    </div>

    {% if records %}
    <div class="table-wrap">
      <table class="history-table">
        <thead>
          <tr><th>#</th><th>Name</th><th>Qualification</th><th>Top Skill</th><th>Score</th><th>Demand</th><th>Date</th></tr>
        </thead>
        <tbody>
          {% for r in records %}
          <tr>
            <td>{{ loop.index }}</td>
            <td><strong>{{ r[0] }}</strong></td>
            <td>{{ r[1] or '&mdash;' }}</td>
            <td><span class="skill-badge">{{ r[2] }}</span></td>
            <td>
              <div class="mini-bar-track"><div class="mini-bar-fill" style="width:{{ r[3] }}%"></div></div>
              <small>{{ r[3] }}%</small>
            </td>
            <td><span class="demand-badge demand-{{ r[4].lower().replace(' ','-') }}">{{ r[4] }}</span></td>
            <td><small>{{ r[5][:10] }}</small></td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
    {% else %}
    <div class="empty-state">
      <div class="empty-icon">&#128235;</div>
      <h3>No history yet</h3>
      <p>Analyse a profile to see results here.</p>
      <a href="/" class="cta-btn">Start Now &#8594;</a>
    </div>
    {% endif %}

    <div style="margin-top:3rem;text-align:center">
      <a href="/" class="cta-btn">&#8592; New Analysis</a>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="container">
    <div class="footer-inner">
      <span class="logo">Skill<span>Sense</span></span>
      <span class="footer-note">Built with Python &middot; Flask &middot; TF-IDF &middot; SQLite</span>
    </div>
  </div>
</footer>
</body>
</html>
"""

# ══════════════════════════════════════════════════════════════
#  STYLE.CSS
# ══════════════════════════════════════════════════════════════
CSS = r"""@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,700;0,900;1,700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

:root{
  --night:#060a12;--deep:#0a1020;--surface:#0f1a2e;--card:#111d33;--card-hover:#162240;
  --rim:rgba(255,255,255,0.06);--rim-strong:rgba(255,255,255,0.12);
  --gold:#d4a843;--gold-light:#f0c866;--gold-dim:rgba(212,168,67,0.15);
  --teal:#00c9a7;--teal-dim:rgba(0,201,167,0.12);
  --sky:#4d9fff;--sky-dim:rgba(77,159,255,0.12);--rose:#ff6b8a;
  --text:#e8edf5;--text-muted:#6b7a99;--text-soft:#a0aec0;
  --ff-display:'Playfair Display',Georgia,serif;
  --ff-body:'Plus Jakarta Sans',sans-serif;
  --r-sm:10px;--r-md:16px;--r-lg:22px;--r-xl:32px;
  --shadow-gold:0 0 40px rgba(212,168,67,0.18);
  --shadow-card:0 8px 48px rgba(0,0,0,0.5);
}

*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--night);color:var(--text);font-family:var(--ff-body);font-size:16px;line-height:1.7;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");opacity:0.025;pointer-events:none;z-index:9999}
a{color:inherit;text-decoration:none}
.container{max-width:1200px;margin:0 auto;padding:0 2rem}

/* NAV */
.nav{position:fixed;top:0;left:0;right:0;z-index:500;background:rgba(6,10,18,0.85);backdrop-filter:blur(20px);border-bottom:1px solid var(--rim)}
.nav::after{content:'';position:absolute;bottom:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent);opacity:0.4}
.nav-inner{max-width:1200px;margin:0 auto;padding:1.1rem 2rem;display:flex;align-items:center;justify-content:space-between}
.logo{font-family:var(--ff-display);font-weight:700;font-size:1.45rem;letter-spacing:0.5px}
.logo span{color:var(--gold);font-style:italic}
.nav-links{display:flex;gap:2.5rem;align-items:center}
.nav-links a{font-size:0.82rem;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;color:var(--text-muted);transition:color .25s;position:relative}
.nav-links a::after{content:'';position:absolute;bottom:-4px;left:0;right:0;height:1px;background:var(--gold);transform:scaleX(0);transition:transform .25s}
.nav-links a:hover{color:var(--gold)}.nav-links a:hover::after,.nav-links a.active::after{transform:scaleX(1)}.nav-links a.active{color:var(--gold)}

/* BLOBS */
.blob{position:absolute;border-radius:50%;filter:blur(120px);opacity:0.22;pointer-events:none;animation:pulse-blob 8s ease-in-out infinite alternate}
.b1{width:700px;height:700px;background:#1a3a8a;top:-300px;right:-200px;animation-delay:0s}
.b2{width:500px;height:500px;background:#0a5a46;bottom:-200px;left:-150px;animation-delay:3s}
.b3{width:400px;height:400px;background:#7a3a00;top:100px;left:30%;animation-delay:6s;opacity:0.12}
@keyframes pulse-blob{0%{transform:scale(1) translate(0,0)}100%{transform:scale(1.15) translate(30px,-20px)}}
.grid-overlay{position:absolute;inset:0;background-image:linear-gradient(rgba(212,168,67,0.025) 1px,transparent 1px),linear-gradient(90deg,rgba(212,168,67,0.025) 1px,transparent 1px);background-size:80px 80px}

/* HERO */
.hero{position:relative;min-height:100vh;display:flex;align-items:center;padding:9rem 2rem 5rem;overflow:hidden}
.hero-bg{position:absolute;inset:0;overflow:hidden}
.hero-content{position:relative;z-index:2;max-width:680px;padding-left:max(0px,calc((100vw - 1200px)/2))}

.badge{display:inline-flex;align-items:center;gap:0.5rem;padding:0.45rem 1.1rem;border-radius:100px;background:var(--gold-dim);border:1px solid rgba(212,168,67,0.3);font-size:0.7rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--gold-light);margin-bottom:2rem;animation:fade-in-down 0.6s ease both}
h1{font-family:var(--ff-display);font-size:clamp(3rem,7vw,5.5rem);font-weight:900;line-height:1.05;letter-spacing:-1px;margin-bottom:1.5rem;animation:fade-in-up 0.7s 0.1s ease both}
.gradient-text{background:linear-gradient(135deg,var(--gold-light) 0%,var(--teal) 60%,var(--sky) 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;font-style:italic}
.hero-sub{font-size:1.1rem;color:var(--text-soft);max-width:500px;margin-bottom:2.8rem;line-height:1.85;animation:fade-in-up 0.7s 0.2s ease both}
.cta-btn{display:inline-flex;align-items:center;gap:0.8rem;padding:1rem 2.2rem;background:linear-gradient(135deg,var(--gold) 0%,#b8860b 100%);color:#0a0a0a;border-radius:100px;font-family:var(--ff-body);font-weight:700;font-size:0.9rem;letter-spacing:0.04em;transition:transform .25s,box-shadow .25s;box-shadow:var(--shadow-gold);animation:fade-in-up 0.7s 0.3s ease both;cursor:pointer}
.cta-btn svg{width:18px;height:18px}
.cta-btn:hover{transform:translateY(-3px);box-shadow:0 0 60px rgba(212,168,67,0.45)}

/* FLOATING CARDS */
.floating-cards{position:absolute;right:max(2rem,calc((100vw - 1200px)/2));top:50%;transform:translateY(-50%);display:flex;flex-direction:column;gap:1rem;z-index:2}
.fc{display:flex;align-items:center;gap:0.9rem;background:var(--card);border:1px solid var(--rim-strong);border-radius:var(--r-md);padding:0.9rem 1.4rem;font-size:0.85rem;font-weight:500;color:var(--text-soft);backdrop-filter:blur(10px);animation:float 5s ease-in-out infinite;box-shadow:var(--shadow-card);transition:border-color .3s}
.fc:hover{border-color:rgba(212,168,67,0.3);color:var(--text)}
.fc1{animation-delay:0s}.fc2{animation-delay:1s}.fc3{animation-delay:2s}.fc4{animation-delay:3s}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}

/* KEYFRAMES */
@keyframes fade-in-up{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}
@keyframes fade-in-down{from{opacity:0;transform:translateY(-16px)}to{opacity:1;transform:translateY(0)}}
@keyframes fade-up{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}

/* HOW */
.how-section{padding:7rem 0;background:var(--deep);border-top:1px solid var(--rim);position:relative}
.how-section::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent);opacity:0.3}
.section-label{font-size:0.7rem;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:var(--gold);margin-bottom:0.8rem;display:flex;align-items:center;gap:0.7rem}
.section-label::before{content:'';display:inline-block;width:24px;height:1px;background:var(--gold);flex-shrink:0}
.section-title{font-family:var(--ff-display);font-size:clamp(2rem,3.5vw,3rem);font-weight:700;letter-spacing:-0.5px;margin-bottom:3.5rem;line-height:1.2}
.steps{display:flex;align-items:stretch;gap:1.2rem}
.step{flex:1;background:var(--card);border:1px solid var(--rim);border-radius:var(--r-lg);padding:2.5rem 2rem;transition:border-color .3s,transform .35s,box-shadow .35s;cursor:default}
.step:hover{border-color:rgba(212,168,67,0.35);transform:translateY(-6px);box-shadow:0 20px 60px rgba(0,0,0,0.4)}
.step-num{font-family:var(--ff-display);font-size:4rem;font-weight:900;line-height:1;margin-bottom:1.2rem;color:var(--gold);opacity:0.3}
.step-body h3{font-family:var(--ff-display);font-size:1.2rem;font-weight:700;margin-bottom:0.7rem;color:var(--text)}
.step-body p{font-size:0.9rem;color:var(--text-muted);line-height:1.75}
.step-arrow{display:flex;align-items:center;justify-content:center;color:var(--gold);opacity:0.25;font-size:1.5rem;flex-shrink:0}

/* FORM */
.form-section{padding:7rem 0 9rem;background:var(--night);position:relative}
.form-section::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,var(--teal),transparent);opacity:0.3}
.form-wrap{max-width:860px;margin:0 auto}
.form-header{margin-bottom:3.5rem}
.form-header p{color:var(--text-muted);margin-top:0.6rem;font-size:0.95rem}
.skill-form{display:flex;flex-direction:column;gap:2rem}
.form-row{display:flex;flex-direction:column;gap:2rem}
.two-col{flex-direction:row;gap:2rem}
.two-col .field-group{flex:1}
.field-group{display:flex;flex-direction:column;gap:0.55rem}
.field-group label{font-size:0.75rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--text-soft)}
.field-group input{background:var(--card);border:1px solid var(--rim);border-radius:var(--r-sm);padding:0.95rem 1.2rem;color:var(--text);font-family:var(--ff-body);font-size:0.95rem;outline:none;transition:border-color .25s,box-shadow .25s,background .25s;width:100%}
.field-group input::placeholder{color:var(--text-muted);opacity:0.5}
.field-group input:focus{border-color:var(--gold);background:var(--card-hover);box-shadow:0 0 0 3px rgba(212,168,67,0.1)}
.field-group small{font-size:0.73rem;color:var(--text-muted)}
.form-submit{padding-top:0.5rem}
.submit-btn{display:inline-flex;align-items:center;gap:0.75rem;padding:1.1rem 2.8rem;background:linear-gradient(135deg,var(--gold) 0%,#b8860b 100%);color:#0a0a0a;border:none;border-radius:100px;font-family:var(--ff-body);font-size:0.95rem;font-weight:700;letter-spacing:0.05em;cursor:pointer;transition:transform .25s,box-shadow .25s,opacity .2s;box-shadow:var(--shadow-gold)}
.submit-btn:hover{transform:translateY(-3px);box-shadow:0 0 60px rgba(212,168,67,0.5)}
.submit-btn:disabled{opacity:0.55;cursor:not-allowed;transform:none}

/* RESULT */
.result-page{background:var(--night)}
.result-hero{position:relative;padding:9rem 0 4rem;overflow:hidden}
.rh-bg{position:absolute;inset:0;overflow:hidden}

/* TOP PICK */
.top-pick-section{padding:3rem 0}
.top-pick-card{display:grid;grid-template-columns:1fr 1.6fr;background:var(--card);border:1px solid rgba(212,168,67,0.25);border-radius:var(--r-xl);overflow:hidden;box-shadow:var(--shadow-card),var(--shadow-gold);position:relative}
.top-pick-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--gold),var(--teal),var(--sky));z-index:1}
.tp-left{padding:3rem;background:linear-gradient(160deg,var(--card-hover),var(--card));border-right:1px solid var(--rim);display:flex;flex-direction:column;justify-content:center}
.tp-right{padding:3rem}
.tp-label{font-size:0.68rem;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:var(--gold);margin-bottom:0.8rem}
.tp-skill{font-family:var(--ff-display);font-size:clamp(2rem,4vw,3.2rem);font-weight:900;letter-spacing:-1px;line-height:1.1;margin-bottom:2rem}
.tp-score-bar-wrap{margin-bottom:2rem}
.tp-score-label{font-size:0.68rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--text-muted);margin-bottom:0.6rem}
.tp-bar-track{height:8px;background:var(--surface);border-radius:100px;overflow:hidden;margin-bottom:0.6rem}
.tp-bar-fill{height:100%;background:linear-gradient(90deg,var(--gold),var(--teal));border-radius:100px;box-shadow:0 0 12px rgba(212,168,67,0.4)}
.tp-score-num{font-family:var(--ff-display);font-size:2.2rem;font-weight:900;color:var(--gold-light);line-height:1}
.tp-tags{display:flex;gap:0.7rem;flex-wrap:wrap}
.tag{padding:0.4rem 1rem;border-radius:100px;font-size:0.73rem;font-weight:600;letter-spacing:0.04em}
.tag-demand{background:var(--teal-dim);color:var(--teal);border:1px solid rgba(0,201,167,0.3)}
.tag-salary{background:var(--gold-dim);color:var(--gold-light);border:1px solid rgba(212,168,67,0.3)}
.tp-section-label,.tp-careers-label{font-size:0.68rem;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:var(--text-muted);margin-bottom:0.8rem;display:flex;align-items:center;gap:0.6rem}
.tp-section-label::before,.tp-careers-label::before{content:'';width:16px;height:1px;background:var(--text-muted);display:inline-block;flex-shrink:0}
.tp-careers-label{margin-top:1.8rem}
.tp-explanation{font-size:0.96rem;color:var(--text-soft);line-height:1.9}
.tp-careers{display:flex;gap:0.5rem;flex-wrap:wrap}
.career-chip{padding:0.35rem 0.9rem;background:var(--sky-dim);border:1px solid rgba(77,159,255,0.2);border-radius:100px;font-size:0.76rem;font-weight:500;color:var(--sky)}

/* RECS */
.recs-section{padding:4rem 0 7rem}
.recs-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:1.5rem;margin-top:3rem}
.rec-card{background:var(--card);border:1px solid var(--rim);border-radius:var(--r-lg);padding:2rem;transition:border-color .3s,transform .3s,box-shadow .3s;animation:fade-up 0.5s ease both;position:relative;overflow:hidden}
.rec-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--gold),transparent);opacity:0;transition:opacity .3s}
.rec-card:hover::before{opacity:1}
.rec-card:hover{border-color:rgba(212,168,67,0.3);transform:translateY(-5px);box-shadow:var(--shadow-card)}
.rec-card--top{border-color:rgba(212,168,67,0.22);background:linear-gradient(160deg,var(--card-hover),var(--card))}
.rec-card--top::before{opacity:0.6}
.rc-header{display:flex;align-items:center;gap:0.9rem;margin-bottom:1.2rem}
.rc-rank{width:32px;height:32px;border-radius:50%;background:var(--gold-dim);border:1px solid rgba(212,168,67,0.25);display:flex;align-items:center;justify-content:center;font-size:0.75rem;font-weight:700;color:var(--gold);flex-shrink:0}
.rc-skill{font-family:var(--ff-display);font-size:1.15rem;font-weight:700;flex:1;line-height:1.2}
.rc-score{font-family:var(--ff-display);font-size:1.2rem;font-weight:900;color:var(--gold-light)}
.rc-bar-track{height:4px;background:var(--surface);border-radius:100px;overflow:hidden;margin-bottom:1.2rem}
.rc-bar-fill{height:100%;background:linear-gradient(90deg,var(--gold),var(--teal));border-radius:100px}
.rc-desc{font-size:0.875rem;color:var(--text-muted);line-height:1.75;margin-bottom:1.2rem}
.rc-meta{display:flex;gap:1.5rem;margin-bottom:1.2rem;padding-bottom:1.2rem;border-bottom:1px solid var(--rim)}
.rc-meta-item{font-size:0.82rem;color:var(--text-soft);font-weight:500}
.rc-expand{font-size:0.85rem}
.rc-expand summary{cursor:pointer;color:var(--gold);font-weight:600;font-size:0.78rem;letter-spacing:0.06em;text-transform:uppercase;list-style:none;display:flex;align-items:center;gap:0.5rem;padding:0.3rem 0;transition:color .2s}
.rc-expand summary::-webkit-details-marker{display:none}
.rc-expand summary::before{content:'▸';transition:transform .2s;font-size:0.65rem}
.rc-expand[open] summary::before{transform:rotate(90deg)}
.rc-expand summary:hover{color:var(--gold-light)}
.rc-explanation{padding:1rem 0 0.5rem;color:var(--text-muted);line-height:1.85;font-size:0.875rem}
.rc-careers{display:flex;gap:0.4rem;flex-wrap:wrap;padding-bottom:0.5rem}

/* PROFILE SUMMARY */
.profile-summary-section{padding:4rem 0 7rem;background:var(--deep);border-top:1px solid var(--rim)}
.ps-card{background:var(--card);border:1px solid var(--rim);border-radius:var(--r-xl);padding:3rem;max-width:860px;margin:0 auto;box-shadow:var(--shadow-card)}
.ps-card h3{font-family:var(--ff-display);font-size:1.6rem;font-weight:700;margin-bottom:1.8rem}
.ps-grid{display:flex;flex-direction:column;gap:0.7rem}
.ps-item{display:flex;gap:1.5rem;padding:0.85rem 1.2rem;background:var(--surface);border-radius:var(--r-sm);font-size:0.9rem;flex-wrap:wrap;border:1px solid var(--rim);transition:border-color .2s}
.ps-item:hover{border-color:var(--rim-strong)}
.ps-key{font-weight:700;color:var(--gold);min-width:150px;font-size:0.77rem;letter-spacing:0.06em;text-transform:uppercase}
.ps-val{color:var(--text-soft)}

/* HISTORY */
.history-section{padding:3rem 0 7rem}
.stats-row{display:flex;gap:1.5rem;margin-bottom:3rem;flex-wrap:wrap}
.stat-card{flex:1;min-width:160px;background:var(--card);border:1px solid var(--rim);border-radius:var(--r-lg);padding:2rem;text-align:center;transition:border-color .3s,transform .3s;position:relative;overflow:hidden}
.stat-card::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--gold),var(--teal));opacity:0;transition:opacity .3s}
.stat-card:hover{border-color:rgba(212,168,67,0.3);transform:translateY(-4px)}
.stat-card:hover::after{opacity:1}
.stat-num{font-family:var(--ff-display);font-size:2.8rem;font-weight:900;color:var(--gold-light);line-height:1;margin-bottom:0.5rem}
.stat-label{font-size:0.72rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--text-muted)}
.table-wrap{overflow-x:auto;border-radius:var(--r-lg);border:1px solid var(--rim);box-shadow:var(--shadow-card)}
.history-table{width:100%;border-collapse:collapse;font-size:0.88rem}
.history-table thead tr{background:var(--card-hover);border-bottom:1px solid var(--rim-strong)}
.history-table th{padding:1.1rem 1.4rem;text-align:left;font-size:0.68rem;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:var(--text-muted)}
.history-table td{padding:1rem 1.4rem;border-bottom:1px solid var(--rim);vertical-align:middle;color:var(--text-soft)}
.history-table tr:last-child td{border-bottom:none}
.history-table tbody tr{transition:background .2s}
.history-table tbody tr:hover td{background:rgba(212,168,67,0.03);color:var(--text)}
.skill-badge{padding:0.3rem 0.85rem;background:var(--gold-dim);border:1px solid rgba(212,168,67,0.25);border-radius:100px;color:var(--gold-light);font-size:0.76rem;font-weight:600;white-space:nowrap}
.mini-bar-track{height:4px;background:var(--surface);border-radius:100px;overflow:hidden;margin-bottom:3px;width:90px}
.mini-bar-fill{height:100%;background:linear-gradient(90deg,var(--gold),var(--teal));border-radius:100px}
.demand-badge{padding:0.28rem 0.75rem;border-radius:100px;font-size:0.7rem;font-weight:700;letter-spacing:0.05em;white-space:nowrap}
.demand-very-high{background:var(--teal-dim);color:var(--teal);border:1px solid rgba(0,201,167,0.25)}
.demand-high{background:var(--sky-dim);color:var(--sky);border:1px solid rgba(77,159,255,0.25)}
.demand-medium{background:rgba(255,170,0,0.1);color:#ffaa00;border:1px solid rgba(255,170,0,0.25)}
.demand-low{background:rgba(255,107,138,0.1);color:var(--rose);border:1px solid rgba(255,107,138,0.25)}
.empty-state{text-align:center;padding:6rem 1rem;color:var(--text-muted)}
.empty-icon{font-size:3.5rem;margin-bottom:1.2rem}
.empty-state h3{font-family:var(--ff-display);font-size:1.6rem;color:var(--text);margin-bottom:0.6rem}
.empty-state p{margin-bottom:2rem}

/* FOOTER */
.footer{border-top:1px solid var(--rim);padding:2.2rem 0;background:var(--deep);position:relative}
.footer::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent);opacity:0.25}
.footer-inner{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem}
.footer-note{font-size:0.78rem;color:var(--text-muted);letter-spacing:0.04em}

/* NAV USER / LOGOUT */
.nav-user{font-size:0.78rem;font-weight:600;letter-spacing:0.08em;color:var(--gold);opacity:0.85;text-transform:uppercase}
.nav-logout{font-size:0.78rem;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;color:var(--rose)!important;border:1px solid rgba(255,107,138,0.3);border-radius:6px;padding:0.3rem 0.9rem;transition:all .25s}
.nav-logout:hover{background:rgba(255,107,138,0.12);border-color:var(--rose)}

/* AUTH PAGES */
.auth-page{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:2rem;position:relative;overflow:hidden}
.auth-bg{position:fixed;inset:0;z-index:0}
.auth-card{position:relative;z-index:2;background:var(--card);border:1px solid var(--rim-strong);border-radius:var(--r-xl);padding:3rem 2.8rem;width:100%;max-width:440px;box-shadow:var(--shadow-card),0 0 80px rgba(212,168,67,0.08)}
.auth-card::before{content:'';position:absolute;inset:0;border-radius:var(--r-xl);background:linear-gradient(135deg,rgba(212,168,67,0.04),transparent 60%);pointer-events:none}
.auth-logo{font-family:var(--ff-display);font-weight:700;font-size:1.6rem;text-align:center;margin-bottom:0.4rem}
.auth-logo span{color:var(--gold);font-style:italic}
.auth-subtitle{text-align:center;color:var(--text-muted);font-size:0.88rem;margin-bottom:2rem;letter-spacing:0.02em}
.auth-title{font-family:var(--ff-display);font-size:1.5rem;font-weight:700;margin-bottom:0.3rem;text-align:center}
.auth-field{margin-bottom:1.3rem}
.auth-field label{display:block;font-size:0.8rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;color:var(--text-muted);margin-bottom:0.55rem}
.auth-field input{width:100%;background:rgba(255,255,255,0.04);border:1px solid var(--rim-strong);border-radius:var(--r-sm);padding:0.85rem 1rem;color:var(--text);font-family:var(--ff-body);font-size:0.95rem;outline:none;transition:border-color .25s,box-shadow .25s}
.auth-field input:focus{border-color:var(--gold);box-shadow:0 0 0 3px rgba(212,168,67,0.1)}
.auth-field input.error-field{border-color:var(--rose);box-shadow:0 0 0 3px rgba(255,107,138,0.1)}
.auth-error{background:rgba(255,107,138,0.1);border:1px solid rgba(255,107,138,0.3);border-radius:8px;padding:0.7rem 1rem;font-size:0.85rem;color:#ffb3c0;margin-top:0.5rem;display:flex;align-items:center;gap:0.5rem}
.auth-error::before{content:'⚠';font-size:0.9rem}
.auth-success{background:rgba(0,201,167,0.1);border:1px solid rgba(0,201,167,0.3);border-radius:8px;padding:0.7rem 1rem;font-size:0.85rem;color:#7fffd4;margin-bottom:1.2rem}
.auth-btn{width:100%;background:linear-gradient(135deg,var(--gold),var(--gold-light));color:#0a0a0a;font-family:var(--ff-body);font-size:0.95rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;border:none;border-radius:var(--r-sm);padding:0.95rem;cursor:pointer;transition:all .25s;margin-top:0.4rem}
.auth-btn:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(212,168,67,0.35)}
.auth-links{display:flex;flex-direction:column;gap:0.6rem;margin-top:1.5rem;text-align:center}
.auth-links a{font-size:0.85rem;color:var(--text-muted);transition:color .2s}
.auth-links a:hover{color:var(--gold)}
.auth-links a span{color:var(--gold);font-weight:600}
.auth-divider{border:none;border-top:1px solid var(--rim);margin:1.5rem 0}
.token-box{background:rgba(212,168,67,0.08);border:1px solid rgba(212,168,67,0.25);border-radius:10px;padding:1rem 1.2rem;margin:1rem 0}
.token-box p{font-size:0.82rem;color:var(--text-muted);margin-bottom:0.4rem}
.token-code{font-family:monospace;font-size:1.1rem;color:var(--gold);letter-spacing:0.15em;font-weight:700}

::-webkit-scrollbar{width:6px}
::-webkit-scrollbar-track{background:var(--night)}
::-webkit-scrollbar-thumb{background:var(--rim-strong);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:rgba(212,168,67,0.3)}
::selection{background:rgba(212,168,67,0.3);color:var(--text)}

/* RESPONSIVE */
@media(max-width:960px){.top-pick-card{grid-template-columns:1fr}.tp-left{border-right:none;border-bottom:1px solid var(--rim)}.floating-cards{display:none}.hero-content{max-width:100%;padding-left:0}.two-col{flex-direction:column}.step-arrow{display:none}.steps{flex-direction:column;gap:1.2rem}}
@media(max-width:640px){h1{letter-spacing:-0.5px}.nav-links{gap:1.5rem}.recs-grid{grid-template-columns:1fr}.stats-row{flex-direction:column}.hero{padding:8rem 1.5rem 4rem}.container{padding:0 1.2rem}.ps-card{padding:1.8rem}.tp-left,.tp-right{padding:2rem}}
"""

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Sign In &mdash; SkillSense</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}"/>
</head>
<body>
<div class="auth-bg">
  <div class="blob b1"></div><div class="blob b2"></div><div class="grid-overlay" style="position:fixed;inset:0;opacity:0.4"></div>
</div>
<div class="auth-page">
  <div class="auth-card">
    <div class="auth-logo">Skill<span>Sense</span></div>
    <div class="auth-subtitle">AI Career Path Recommender</div>
    <div class="auth-title">Welcome Back</div>
    <p style="text-align:center;color:var(--text-muted);font-size:0.85rem;margin-bottom:1.8rem">Sign in to continue to your dashboard</p>
    <form method="POST" action="/login">
      <div class="auth-field">
        <label>Username</label>
        <input type="text" name="username" placeholder="Enter your username" required autocomplete="username" class="{{ 'error-field' if error_user else '' }}"/>
        {% if error_user %}<div class="auth-error">{{ error_user }}</div>{% endif %}
      </div>
      <div class="auth-field">
        <label>Password</label>
        <input type="password" name="password" placeholder="Enter your password" required autocomplete="current-password" class="{{ 'error-field' if error_pass else '' }}"/>
        {% if error_pass %}<div class="auth-error">{{ error_pass }}</div>{% endif %}
      </div>
      <button type="submit" class="auth-btn">Sign In &rarr;</button>
    </form>
    <hr class="auth-divider"/>
    <div class="auth-links">
      <a href="/signup">Don't have an account? <span>Sign Up</span></a>
      <a href="/forgot-password">Forgot your password?</a>
    </div>
  </div>
</div>
</body>
</html>
"""

SIGNUP_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Sign Up &mdash; SkillSense</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}"/>
</head>
<body>
<div class="auth-bg">
  <div class="blob b1"></div><div class="blob b2"></div><div class="grid-overlay" style="position:fixed;inset:0;opacity:0.4"></div>
</div>
<div class="auth-page">
  <div class="auth-card">
    <div class="auth-logo">Skill<span>Sense</span></div>
    <div class="auth-subtitle">AI Career Path Recommender</div>
    <div class="auth-title">Create Account</div>
    <p style="text-align:center;color:var(--text-muted);font-size:0.85rem;margin-bottom:1.8rem">Join SkillSense and discover your perfect skill path</p>
    {% if error %}<div class="auth-error" style="margin-bottom:1rem">{{ error }}</div>{% endif %}
    <form method="POST" action="/signup">
      <div class="auth-field">
        <label>Username</label>
        <input type="text" name="username" placeholder="Choose a username (min 3 chars)" required autocomplete="username" minlength="3"/>
      </div>
      <div class="auth-field">
        <label>Password</label>
        <input type="password" name="password" placeholder="Create a password (min 6 chars)" required autocomplete="new-password" minlength="6"/>
      </div>
      <div class="auth-field">
        <label>Confirm Password</label>
        <input type="password" name="password2" placeholder="Repeat your password" required autocomplete="new-password"/>
      </div>
      <button type="submit" class="auth-btn">Create Account &rarr;</button>
    </form>
    <hr class="auth-divider"/>
    <div class="auth-links">
      <a href="/login">Already have an account? <span>Sign In</span></a>
    </div>
  </div>
</div>
</body>
</html>
"""

FORGOT_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Forgot Password &mdash; SkillSense</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}"/>
</head>
<body>
<div class="auth-bg">
  <div class="blob b1"></div><div class="blob b2"></div><div class="grid-overlay" style="position:fixed;inset:0;opacity:0.4"></div>
</div>
<div class="auth-page">
  <div class="auth-card">
    <div class="auth-logo">Skill<span>Sense</span></div>
    <div class="auth-subtitle">AI Career Path Recommender</div>
    <div class="auth-title">Reset Password</div>

    {% if message == "reset_ok" %}
      <div class="auth-success" style="margin-top:1rem">&#10003; Password reset successfully! <a href="/login" style="color:var(--gold)">Sign In</a></div>
    {% elif message == "not_found" %}
      <div class="auth-error" style="margin-bottom:1rem">Username not found.</div>
    {% elif message == "mismatch" %}
      <div class="auth-error" style="margin-bottom:1rem">Passwords do not match.</div>
    {% elif message == "short" %}
      <div class="auth-error" style="margin-bottom:1rem">Password must be at least 6 characters.</div>
    {% elif message == "bad_token" %}
      <div class="auth-error" style="margin-bottom:1rem">Invalid username or recovery token.</div>
    {% endif %}

    {% if message == "success" and token_info %}
      <div class="auth-success">Username verified. Use the recovery token below to reset your password.</div>
      <div class="token-box">
        <p>Your recovery token for <strong>{{ token_info.username }}</strong>:</p>
        <div class="token-code">{{ token_info.token }}</div>
        <p style="font-size:0.75rem;margin-top:0.5rem;color:var(--text-muted)">Copy this token and enter it below.</p>
      </div>
      <form method="POST" action="/forgot-password">
        <input type="hidden" name="action" value="reset"/>
        <div class="auth-field">
          <label>Username</label>
          <input type="text" name="username" value="{{ token_info.username }}" required/>
        </div>
        <div class="auth-field">
          <label>Recovery Token</label>
          <input type="text" name="token" placeholder="Paste your recovery token" required/>
        </div>
        <div class="auth-field">
          <label>New Password</label>
          <input type="password" name="new_password" placeholder="New password (min 6 chars)" required minlength="6"/>
        </div>
        <div class="auth-field">
          <label>Confirm New Password</label>
          <input type="password" name="new_password2" placeholder="Repeat new password" required/>
        </div>
        <button type="submit" class="auth-btn">Reset Password &rarr;</button>
      </form>
    {% elif message != "reset_ok" %}
      <p style="text-align:center;color:var(--text-muted);font-size:0.85rem;margin-bottom:1.8rem">Enter your username to get a recovery token</p>
      <form method="POST" action="/forgot-password">
        <input type="hidden" name="action" value="request"/>
        <div class="auth-field">
          <label>Username</label>
          <input type="text" name="username" placeholder="Your SkillSense username" required/>
        </div>
        <button type="submit" class="auth-btn">Get Recovery Token &rarr;</button>
      </form>
    {% endif %}

    <hr class="auth-divider"/>
    <div class="auth-links">
      <a href="/login">Back to <span>Sign In</span></a>
    </div>
  </div>
</div>
</body>
</html>
"""

# ══════════════════════════════════════════════════════════════
#  WRITE ALL FILES
# ══════════════════════════════════════════════════════════════
print(f"\n{'='*55}")
print(f"  SkillSense Setup v2 — Creating project files")
print(f"{'='*55}")
print(f"\n  Folder: {BASE}\n")

w("dataset.csv",              DATASET)
w("model.py",                 MODEL_PY)
w("app.py",                   APP_PY)
w("requirements.txt",         "flask>=2.3.0\npandas>=2.0.0\nscikit-learn>=1.3.0\nnumpy>=1.24.0\n")
w("templates/index.html",         INDEX_HTML)
w("templates/result.html",        RESULT_HTML)
w("templates/history.html",       HISTORY_HTML)
w("templates/login.html",         LOGIN_HTML)
w("templates/signup.html",        SIGNUP_HTML)
w("templates/forgot_password.html", FORGOT_HTML)
w("static/style.css",             CSS)

# ══════════════════════════════════════════════════════════════
#  INSTALL DEPENDENCIES
# ══════════════════════════════════════════════════════════════
print("\n  Installing dependencies...")
subprocess.check_call([sys.executable, "-m", "pip", "install",
                       "flask", "pandas", "scikit-learn", "numpy", "-q"])
print("  ✔  Dependencies ready")

# ══════════════════════════════════════════════════════════════
#  LAUNCH
# ══════════════════════════════════════════════════════════════
print(f"\n{'='*55}")
print(f"  Launching SkillSense at  http://127.0.0.1:5000")
print(f"  Press Ctrl+C to stop")
print(f"{'='*55}\n")

os.chdir(BASE)
subprocess.run([sys.executable, "app.py"])
