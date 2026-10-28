from analyzer import analyze_resume

resume_text = "Python AWS GitHub"

job_description = "Python AWS Docker Terraform"

result = analyze_resume(
    resume_text,
    job_description
)

print("=" * 60)
print("AI ANALYSIS")
print("=" * 60)
print(result)
print("=" * 60)