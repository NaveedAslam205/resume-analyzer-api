import re

def extract_profile_info(text: str):
    email_match = re.search(r"[\w\.-]+@[\w\.-]+", text)
    linkedin_match = re.search(r"(https?:\/\/)?(www\.)?linkedin\.com\/in\/[A-z0-9_-]+", text)

    return {
        "email": email_match.group() if email_match else None,
        "linkedin_url": linkedin_match.group() if linkedin_match else None
    }
