from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from ats_scoring import score_resume_against_jd
from lie_detector import detect_lies
import fitz  # PyMuPDF

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze-with-jd")
async def analyze_resume(file: UploadFile = File(...), jd: str = Form(...)):
    # Extract text from PDF
    content = await file.read()
    doc = fitz.open(stream=content, filetype="pdf")
    resume_text = ""
    for page in doc:
        resume_text += page.get_text()

    score, suggestions = score_resume_against_jd(resume_text, jd)
    return {
        "score": score,
        "suggestions": suggestions
    }

@app.post("/lie-detection")
async def analyze_lies(file: UploadFile = File(...)):
    content = await file.read()
    doc = fitz.open(stream=content, filetype="pdf")
    resume_text = ""
    for page in doc:
        resume_text += page.get_text()

    issues, confidence = detect_lies(resume_text)
    return {
        "issues": issues,
        "confidence": confidence
    }
