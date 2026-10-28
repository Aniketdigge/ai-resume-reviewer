from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def analyze_resume(resume_text, job_description):

    prompt = f"""
    You are an ATS and Resume Expert.

    Analyze the resume against the provided job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Provide:

    1. ATS Score out of 100
    2. Matching Skills
    3. Missing Skills
    4. Resume Strengths
    5. Resume Weaknesses
    6. Suggestions For Improvement
    """

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text