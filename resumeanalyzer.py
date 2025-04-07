import PyPDF2
import re

# List of important keywords to match in the resume
KEYWORDS = [
    "python", "mysql", "power bi", "excel", "data analysis",
    "data visualization", "machine learning", "communication", "teamwork",
    "leadership", "problem-solving", "big data", "cloud", "api"
]

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    """
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text.lower()
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def analyze_resume(text):
    """
    Analyzes the text for keyword presence.
    """
    matched = []
    for keyword in KEYWORDS:
        if re.search(rf"\b{re.escape(keyword)}\b", text):
            matched.append(keyword)

    score = len(matched) / len(KEYWORDS) * 100
    return matched, round(score, 2)

def main():
    path = input("Enter path to your resume PDF: ")
    resume_text = extract_text_from_pdf(path)

    if resume_text:
        matched_keywords, score = analyze_resume(resume_text)
        print("\n🔍 Resume Analysis Result")
        print("Matched Keywords:", ", ".join(matched_keywords))
        print(f"\n✅ Skill Match Score: {score}%")
        print(f"🚀 Missing Skills: {', '.join([kw for kw in KEYWORDS if kw not in matched_keywords])}")
    else:
        print("❌ Could not analyze resume. Please check the file path or format.")

if __name__ == "__main__":
    main()
