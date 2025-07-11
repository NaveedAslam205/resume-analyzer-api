import re
import spacy

nlp = spacy.load("en_core_web_sm")

def detect_lies(text: str):
    doc = nlp(text)
    issues = []

    orgs = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    titles = [ent.text for ent in doc.ents if ent.label_ == "TITLE"]

    big_tech = {"Google", "Amazon", "Meta", "Apple", "Microsoft"}
    if any(org in big_tech for org in orgs):
        if "certificate" not in text.lower():
            issues.append("Big tech mentioned but no certification found.")

    years = re.findall(r"\b(\d{1,2})\s+years\b", text.lower())
    for y in years:
        if int(y) > 20:
            issues.append(f"Exaggerated experience: {y} years")

    if any(t in ["CTO", "Chief", "CEO"] for t in titles):
        issues.append("High-level title detected, verify credibility.")

    confidence = "High" if len(issues) >= 3 else "Medium" if issues else "Low"
    return issues, confidence
