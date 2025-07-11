# Resume Analyzer API

A FastAPI-based backend that analyzes resumes against job descriptions using NLP and machine learning techniques. It provides ATS scoring, skill matching, LinkedIn/email extraction, and smart discrepancy detection.

---

##Features

- ✅ **ATS Score**: Calculates resume-to-job description compatibility using `sentence-transformers`.
- 🔍 **Smart Discrepancy Detection**: Flags inconsistencies using embeddings.
- 📎 **LinkedIn & Email Extraction**: Extracts contact details using regex.
- 📄 **PDF Parsing**: Uses `PyMuPDF` to extract text from resumes.
- 📊 **Modular Architecture**: Scalable endpoints and logic separation.
- ⚙️ **FastAPI**: Built for speed and documentation out of the box.
