# Resume.py
import streamlit as st, os

def app():
    st.title("📄 Resume")
    resume_file = "Rajesh_Resume.pdf"
    if os.path.exists(resume_file):
        with open(resume_file, "rb") as f:
            st.download_button("Download Resume", f, file_name=resume_file)
    else:
        st.info("Resume not uploaded. Upload file named 'Rajesh_Resume.pdf' in project root.")
