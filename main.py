from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from resume_analysis.ats_scoring import score_resume_against_jd
from resume_analysis.lie_detection import detect_lies
from resume_analysis.profile_extractor import extract_profile_info
from resume_analysis.ai_analysis import generate_ai_feedback
from resume_analysis.profile_extractor import extract_profile_info
import os

import fitz

app = FastAPI()
port = int(os.environ.get("PORT", 10000))
uvicorn.run(app, host="0.0.0.0", port=port)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...), jd: str = Form(...)):
    content = await file.read()
    doc = fitz.open(stream=content, filetype="pdf")
    resume_text = "".join([page.get_text() for page in doc])

    score, suggestions = score_resume_against_jd(resume_text, jd)
    issues, confidence = detect_lies(resume_text)
    profile = extract_profile_info(resume_text)
    ai_feedback = generate_ai_feedback(resume_text, jd)

    return {
        "ats_score": score,
        "suggestions": suggestions,
        "inconsistencies": issues,
        "confidence": confidence,
        "profile": profile,
        "ai_feedback": ai_feedback
    }

@app.post("/profile-check")
async def extract_profile(file: UploadFile = File(...)):
    content = await file.read()
    doc = fitz.open(stream=content, filetype="pdf")
    resume_text = ""
    for page in doc:
        resume_text += page.get_text()

    profile_data = extract_profile_info(resume_text)
    return profile_data
