# Admin.py
import streamlit as st
import json
import os
import hashlib
from datetime import datetime

# ----------------------------
# SIMPLE LOCAL PASSWORD CONFIG
# (no secrets needed)
# ----------------------------
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "2025"  # you can change this anytime


# ----------------------------
# FILE PATHS
# ----------------------------
PROJECTS_FILE = "data/projects.json"
CERTS_FILE = "data/certs.json"
COURSES_FILE = "data/courses.json"
SCREENSHOT_DIR = "data/screenshots"

os.makedirs(SCREENSHOT_DIR, exist_ok=True)


# ----------------------------
# UTILITY FUNCTIONS
# ----------------------------
def load_json(path):
    if not os.path.exists(path):
        return []
    try:
        return json.load(open(path, "r", encoding="utf-8"))
    except:
        return []


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# ----------------------------
# LOGIN
# ----------------------------
def admin_login():
    st.title("🔐 Admin Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            st.session_state["admin_logged_in"] = True
            st.success("Login successful!")
            st.rerun()

        else:
            st.error("Invalid username or password")


# ----------------------------
# DASHBOARD
# ----------------------------
def dashboard():
    st.title("⚡ Admin Dashboard")

    projects = load_json(PROJECTS_FILE)
    certs = load_json(CERTS_FILE)
    courses = load_json(COURSES_FILE)

    col1, col2, col3 = st.columns(3)
    col1.metric("Projects", len(projects))
    col2.metric("Certifications", len(certs))
    col3.metric("Courses", len(courses))

    st.markdown("---")

    section = st.selectbox("Select Section", ["Add Project", "Manage Projects", "Certifications", "Courses"])

    if section == "Add Project":
        add_project_page()
    elif section == "Manage Projects":
        manage_projects_page()
    elif section == "Certifications":
        manage_certs_page()
    else:
        manage_courses_page()


# ----------------------------
# PROJECT MANAGEMENT
# ----------------------------
def add_project_page():
    st.header("➕ Add New Project")

    title = st.text_input("Project Title")
    description = st.text_area("Description")
    link = st.text_input("GitHub / Demo Link")
    screenshot = st.file_uploader("Upload Screenshot", type=["png","jpg","jpeg"])

    if st.button("Add Project"):
        projects = load_json(PROJECTS_FILE)

        item = {
            "id": int(datetime.utcnow().timestamp()),
            "title": title,
            "description": description,
            "link": link
        }

        if screenshot:
            filename = f"{item['id']}_{screenshot.name}"
            path = os.path.join(SCREENSHOT_DIR, filename)
            with open(path, "wb") as f:
                f.write(screenshot.getbuffer())
            item["screenshot"] = path

        projects.append(item)
        save_json(PROJECTS_FILE, projects)
        st.success("Project added!")


def manage_projects_page():
    st.header("🛠 Manage Projects")

    projects = load_json(PROJECTS_FILE)

    if not projects:
        st.info("No projects available.")
        return

    for i, project in enumerate(projects):
        st.subheader(project["title"])
        st.write(project["description"])
        st.write(project["link"])

        if project.get("screenshot"):
            st.image(project["screenshot"], width=350)

        if st.button(f"Delete {project['title']}", key=f"del_{project['id']}"):
            projects.pop(i)
            save_json(PROJECTS_FILE, projects)
            st.warning("Project deleted!")
            st.experimental_rerun()


# ----------------------------
# CERTIFICATIONS
# ----------------------------
def manage_certs_page():
    st.header("🏆 Manage Certifications")

    certs = load_json(CERTS_FILE)

    name = st.text_input("Certification Name")
    org = st.text_input("Issued By")
    link = st.text_input("Certificate Link")

    if st.button("Add Certification"):
        certs.append({"name": name, "org": org, "link": link})
        save_json(CERTS_FILE, certs)
        st.success("Certification added!")

    st.markdown("### All Certifications")
    for c in certs:
        st.write(f"- **{c['name']}** — {c['org']} (`{c['link']}`)")


# ----------------------------
# COURSES
# ----------------------------
def manage_courses_page():
    st.header("🎓 Manage Courses")

    courses = load_json(COURSES_FILE)

    title = st.text_input("Course Title")
    provider = st.text_input("Provider")
    link = st.text_input("Course Link")

    if st.button("Add Course"):
        courses.append({"title": title, "provider": provider, "link": link})
        save_json(COURSES_FILE, courses)
        st.success("Course added!")

    st.markdown("### All Courses")
    for c in courses:
        st.write(f"- **{c['title']}** — {c['provider']} (`{c['link']}`)")


# ----------------------------
# ENTRY POINT
# ----------------------------
def app():
    if "admin_logged_in" not in st.session_state:
        st.session_state["admin_logged_in"] = False

    if not st.session_state["admin_logged_in"]:
        admin_login()
        return

    dashboard()


def dashboard():
    st.title("⚡ Admin Dashboard")

    projects = load_json(PROJECTS_FILE)
    certs = load_json(CERTS_FILE)
    courses = load_json(COURSES_FILE)

    col1, col2, col3 = st.columns(3)
    col1.metric("Projects", len(projects))
    col2.metric("Certifications", len(certs))
    col3.metric("Courses", len(courses))

    st.markdown("---")

    section = st.selectbox("Manage",
                           ["Add Project", "Manage Projects",
                            "Certifications", "Courses",
                            "Resume Manager"])

    if section == "Add Project":
        add_project_page()
    elif section == "Manage Projects":
        manage_projects_page()
    elif section == "Certifications":
        manage_certs_page()
    elif section == "Resume Manager":
        resume_manager()
    else:
        manage_courses_page()



def resume_manager():
    st.header("📄 Resume Manager")

    resume_path = "Rajesh_Resume.pdf"

    # Upload New Resume
    uploaded_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])

    if uploaded_file:
        with open(resume_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("Resume uploaded successfully!")

    # Show Current Resume
    if os.path.exists(resume_path):
        st.markdown("### Current Resume Preview")
        with open(resume_path, "rb") as f:
            st.download_button("Download Resume", f, file_name="Rajesh_Resume.pdf")

        st.info("Resume is available on the Resume page.")
    else:
        st.warning("No resume uploaded yet.")
