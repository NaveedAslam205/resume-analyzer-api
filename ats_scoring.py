import re
from typing import List
import numpy as np

def extract_keywords(text: str) -> List[str]:
    return re.findall(r'\b\w+\b', text.lower())

def score_resume_against_jd(resume_text: str, jd_text: str):
    resume_words = set(extract_keywords(resume_text))
    jd_words = set(extract_keywords(jd_text))

    matched_keywords = resume_words.intersection(jd_words)
    total_keywords = len(jd_words)

    score = int((len(matched_keywords) / total_keywords) * 100) if total_keywords else 0

    missing = jd_words.difference(resume_words)
    suggestions = [f"Add keyword '{kw}'" for kw in list(missing)[:5]]

    return score, suggestions
