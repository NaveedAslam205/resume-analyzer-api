# Resume Analyzer API

A FastAPI-based backend that analyzes resumes against job descriptions using NLP and machine learning techniques. It provides ATS scoring, skill matching, LinkedIn/email extraction, and smart discrepancy detection.

---

## 🚀 Features

- ✅ **ATS Score**: Calculates resume-to-job description compatibility using `sentence-transformers`.
- 🔍 **Smart Discrepancy Detection**: Flags inconsistencies using embeddings.
- 📎 **LinkedIn & Email Extraction**: Extracts contact details using regex.
- 📄 **PDF Parsing**: Uses `PyMuPDF` to extract text from resumes.
- 📊 **Modular Architecture**: Scalable endpoints and logic separation.
- ⚙️ **FastAPI**: Built for speed and documentation out of the box.
- 🌐 **Deployable on Render**: Includes `build.sh` for model download and port setup.

---

## 📁 Project Structure

resume-analyzer-api/
│
├── resume_analysis/
│ ├── ats_scoring.py # Resume-JD similarity with sentence-transformers
│ ├── discrepancy_detection.py # Placeholder for smart resume lie detection
│ ├── extract_info.py # Regex-based LinkedIn/Email extractor
│ └── utils.py # File reading and helper utilities
│
├── main.py # FastAPI app entrypoint
├── build.sh # Custom build script for Render
├── requirements.txt # Optional for local pip installs
├── pyproject.toml # Poetry-based dependency and project management
└── README.md


---

## 🔌 API Endpoints

### 1. POST /analyze
Purpose: Perform full resume analysis including:

ATS score vs JD

Lie/inconsistency detection

Profile extraction (email, LinkedIn)

AI-generated suggestions

Form-Data:

file: resume .pdf file (type: UploadFile)

jd: job description (type: string)

Sample Request:

Headers: Content-Type: multipart/form-data

Body: form-data

Key	Value	Type
file	resume.pdf	File
jd	JD text here	Text

Response:

json
Copy
Edit
{
  "ats_score": 0.82,
  "suggestions": ["Add more leadership keywords", "Include certifications"],
  "inconsistencies": ["Claimed Python experience not supported"],
  "confidence": 0.87,
  "profile": {
    "email": "user@email.com",
    "linkedin": "https://linkedin.com/in/username"
  },
  "ai_feedback": "You should elaborate on your last job’s achievements."
}

