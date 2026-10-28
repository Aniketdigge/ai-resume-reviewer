import streamlit as st

from pdf_reader import extract_resume_text

from analyzer import analyze_resume

st.set_page_config(
    page_title="AI Resume Reviewer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Reviewer")

st.markdown(
    "Upload your resume and compare it against a Job Description using Gemini AI."
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

analyze_button = st.button(
    "Analyze Resume"
)

if analyze_button:

    if not uploaded_file:

        st.warning(
            "Please upload a resume."
        )

    elif not job_description:

        st.warning(
            "Please paste a Job Description."
        )

    else:

        resume_text = extract_resume_text(
            uploaded_file
        )

        with st.spinner(
            "Analyzing Resume..."
        ):

            result = analyze_resume(
                resume_text,
                job_description
            )

        st.success(
            "Analysis Complete!"
        )

        st.markdown(result)