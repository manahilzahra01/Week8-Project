## AI-POWERED RESUME SCREENING & APPLICANT TRACKING SYSTEM (ATS)
 #  Multi-Candidate AI Resume Screening & Hybrid Match Score Dashboard

 # Domain: AI & Machine Learning

# Tools & Libraries: Python, Streamlit, Sentence-BERT (S-BERT), RegEx, Pandas, pdfplumber, Google Colab

## 1. Project Background & Objective
Modern recruitment channels receive hundreds of resumes for a single job opening. Human Resource (HR) teams spend dozens of manual hours reviewing documents, creating severe operational delays. Traditional Applicant Tracking Systems (ATS) use plain keyword searches, which often reject strong candidates simply because they used different phrasing or synonyms.

The primary objective of this project was to design and deploy an End-to-End AI-Driven ATS Platform capable of:

Uploading multiple resumes simultaneously in batch mode.

Extracting critical candidate personal data (Full Name, Email ID, Phone Number) automatically.

Calculating a fair, context-aware Hybrid Match Score based on AI semantic understanding and explicit skill requirements.

Displaying candidate rankings on an interactive, visual web dashboard.

## 2. Technical Stack & Tools Used
Google Colab: Cloud execution environment used to write code, train/load models, and process data.

Streamlit: Python framework used to build the interactive user interface and recruitment dashboard.

Sentence-Transformers (S-BERT): Pre-trained all-MiniLM-L6-v2 neural network used to understand the deep semantic context of resumes and job descriptions.

pdfplumber & RegEx: Libraries used to read text layout from PDF files and parse unstructured strings for candidate contact info.

Pandas: Used to structure result data into sorted tables, leaderboards, and candidate metrics.

## 3. Step-by-Step Project Execution Journey
Our team executed this project through five structured phases:

# Phase 1: Environment Setup & Document Extraction
We set up a Python execution environment in Google Colab and integrated pdfplumber for raw text extraction. This allowed the system to accept both .pdf and .txt resume formats while preserving document structure and removing non-standard characters.

# Phase 2: Candidate Data Parsing Engine 
To eliminate generic labels like "CV-1" or "CV-2" in the leaderboard, we built a rule-based metadata extraction engine:

# Email Extraction: Uses regular expressions to detect email addresses within the resume text.

# Phone Number Extraction: Detects local and international contact numbers using numerical pattern matching.

# Name Extraction: Analyzes header lines and document titles to isolate the candidate's actual full name while filtering out words like "Resume" or "Curriculum Vitae".

## Phase 3: AI Embedding & Semantic Matching
We integrated the Sentence-BERT (all-MiniLM-L6-v2) model. The engine converts both the Job Description and the candidate resumes into 384-dimensional vector spaces. By measuring the angle between these vectors (cosine similarity), the system determines how closely a candidate's background matches the job context—even if exact words do not match.

## Phase 4: Hybrid Scoring Engine
To prevent candidates from artificially inflating scores through keyword padding, we designed a balanced Hybrid Fit Framework:

# 50% Semantic Score: Measures overall conceptual fit and project experience.

# 50% Skill Match Score: Measures the direct coverage of required skills specified by the recruiter.

This combination ensures that candidates who meet core skill prerequisites and possess relevant context receive top leaderboard rankings.

## Phase 5: Dashboard Development & Deployment
We built a responsive web dashboard using Streamlit. The dashboard allows recruiters to:

Paste Job Descriptions and define target skills.

Upload batch resumes simultaneously.

View a sorted Candidate Leaderboard Table containing Names, Emails, Phone Numbers, and Match Percentages.

Inspect individual Candidate Breakdown Cards showing matched skills, missing skill gaps, and auto-detected resume skills.

## 4. System Workflow Diagram
Plaintext
[ Upload Job Description & Target Skills ] ───┐
                                               ├──> [ Streamlit Web UI ]
[ Upload Batch Candidate Resumes (.PDF/.TXT) ] ───┘           │
                                                              ▼
                                              [ Stage 1: Text Extraction (pdfplumber) ]
                                                              │
                                                              ▼
                                              [ Stage 2: Metadata Parser (Name, Email, Phone) ]
                                                              │
                                                              ▼
                                              [ Stage 3: S-BERT Context Encoding & Skill Gap Analysis ]
                                                              │
                                                              ▼
                                              [ Stage 4: 50/50 Hybrid Score Calculation ]
                                                              │
                                                              ▼
                                              [ Ranked Leaderboard & Detailed Breakdown Cards ]


streamlit run app/app.py
## 7. Key Accomplishments & Project Outcomes
Automated Candidate Extraction: Replaced file names (e.g., CV-1, CV-2) with extracted candidate names, emails, and phone numbers.

Objective Ranking: Successfully balanced semantic understanding with exact technical skill matching.

Rapid Batch Processing: Processed multiple resumes in seconds, reducing screening time significantly.

Recruiter-Friendly Interface: Delivered clear skill gap reports showing exactly which skills candidates possess and which ones they lack.
