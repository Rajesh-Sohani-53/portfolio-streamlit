# Projects.py
import json, streamlit as st, os

def app():
    st.title("🚀 My Projects")
    path = "data/projects.json"
    projects = []
    if os.path.exists(path):
        try:
            projects = json.load(open(path, "r", encoding="utf-8"))
        except Exception:
            st.error("projects.json is corrupted")
            return
    if not projects:
        st.info("No projects yet. Add from Admin panel.")
        return

    for p in projects:
        st.markdown(f"<div class='project-card'><h3>{p['title']}</h3><p>{p['description']}</p></div>", unsafe_allow_html=True)
        if p.get("screenshot") and os.path.exists(p["screenshot"]):
            st.image(p["screenshot"], width=380)
        if p.get("link"):
            st.markdown(f"[🔗 View Project]({p['link']})")
