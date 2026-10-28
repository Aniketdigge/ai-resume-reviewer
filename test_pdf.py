"""from pdf_reader import extract_resume_text

pdf_path = "blank.pdf"

resume_text = extract_resume_text(pdf_path)

print(resume_text)"""

from pdf_reader import extract_resume_text

pdf_path = "sample_resume.pdf"

resume_text = extract_resume_text(pdf_path)

print("=" * 50)
print("RESUME TEXT")
print("=" * 50)
print(resume_text)
print("=" * 50)
print("TOTAL CHARACTERS:", len(resume_text))
print("=" * 50)