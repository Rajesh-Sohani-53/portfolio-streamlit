# run_app.py
import streamlit as st
from streamlit_option_menu import option_menu
import os
import Home, Projects, Skills, Contact, Resume, Admin

# ensure data folders exist
os.makedirs("data/screenshots", exist_ok=True)

st.set_page_config(page_title="Rajesh Sohani - Portfolio", layout="wide")

# theme toggle (simple)
if "theme" not in st.session_state:
    st.session_state["theme"] = "dark"

def toggle_theme():
    st.session_state["theme"] = "light" if st.session_state["theme"]=="dark" else "dark"

with st.sidebar:
    st.title("⚡ Rajesh Ravi Sohani")
    st.text("AI/ML Engineer • 2025")
    st.button("🌓 Toggle Theme", on_click=toggle_theme)
    choice = option_menu("Navigation", ["Home","Projects","Skills","Resume","Contact","Admin"],
                         icons=["house","kanban","award","file-earmark-pdf","envelope","gear"],
                         default_index=0)

# load css based on theme
css_path = "styles/dark.css" if st.session_state["theme"]=="dark" else "styles/light.css"
#if os.path.exists(css_path):
    #st.markdown(open(css_path, "r", encoding="utf-8").read(), unsafe_allow_html=True)
#    st.markdown(open(css_path).read(), unsafe_allow_html=True)
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()
st.markdown(css, unsafe_allow_html=True)


if choice == "Home":
    Home.app()
elif choice == "Projects":
    Projects.app()
elif choice == "Skills":
    Skills.app()
elif choice == "Resume":
    Resume.app()
elif choice == "Contact":
    Contact.app()
elif choice == "Admin":
    Admin.app()
