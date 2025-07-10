import re
from typing import List, Tuple

def detect_lies(text: str) -> Tuple[List[str], str]:
    issues = []

    if "CTO" in text or "Chief" in text:
        issues.append("High-ranking title detected. Validate with experience.")
    if re.search(r'\b\d{1,2}\s+years\b', text):
        years = [int(s) for s in re.findall(r'\b\d{1,2}\b', text)]
        if max(years) > 20:
            issues.append("Experience years seem unusually high.")
    if "Google" in text or "Amazon" in text:
        if "certified" not in text.lower():
            issues.append("Big tech company listed with no certifications mentioned.")

    confidence = "Low"
    if len(issues) >= 3:
        confidence = "High"
    elif len(issues) >= 1:
        confidence = "Medium"

    return issues, confidence
