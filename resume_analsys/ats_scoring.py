from sentence_transformers import SentenceTransformer, util
import spacy

nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer("all-MiniLM-L6-v2")

def score_resume_against_jd(resume_text: str, jd_text: str):
    resume_vec = model.encode(resume_text, convert_to_tensor=True)
    jd_vec = model.encode(jd_text, convert_to_tensor=True)
    score = util.cos_sim(resume_vec, jd_vec).item()

    suggestions = []
    lower_resume = resume_text.lower()
    if "education" not in lower_resume:
        suggestions.append("Add an 'Education' section.")
    if "experience" not in lower_resume:
        suggestions.append("Add an 'Experience' section.")
    if "skills" not in lower_resume:
        suggestions.append("Add a 'Skills' section.")

    return round(score * 100, 2), suggestions
