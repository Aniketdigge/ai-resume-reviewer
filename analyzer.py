import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-3.8-flash"
)

def analyze_resume(
    resume_text,
    job_description
):

    prompt = f"""

    You are a Senior ATS Recruiter and Resume Expert.

    Compare the candidate resume with the job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Provide output in the following format:

    ATS Score:
    /100

    Matching Skills:
    - Skill 1
    - Skill 2

    Missing Skills:
    - Skill 1
    - Skill 2

    Strengths:
    - Point 1
    - Point 2

    Weaknesses:
    - Point 1
    - Point 2

    Resume Improvement Suggestions:
    - Action 1
    - Action 2

    Career Recommendation:
    Recommend suitable job roles.

    """

    response = model.generate_content(
        prompt
    )

    return response.text


