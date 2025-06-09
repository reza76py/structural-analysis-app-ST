# file: project_selector.py
import streamlit as st
from data_input.db import get_connection

def fetch_user_projects(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM projects WHERE username = %s", (username,))
    results = cursor.fetchall()
    conn.close()
    return results

def create_new_project(username, project_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projects (username, name) VALUES (%s, %s)", (username, project_name))
    conn.commit()
    project_id = cursor.lastrowid
    conn.close()
    return project_id

def render_project_selector():
    st.subheader("📁 Select or Create a Project")

    username = st.session_state.get("username")
    if not username:
        st.warning("You must be logged in.")
        st.stop()

    # Show existing projects
    projects = fetch_user_projects(username)
    project_names = {f"{name} (ID: {pid})": pid for pid, name in projects}

    if projects:
        selected = st.selectbox("Select an existing project:", list(project_names.keys()))
        if st.button("🔓 Use Selected Project"):
            st.session_state["project_id"] = project_names[selected]
            st.success(f"✅ Project selected: {selected}")
            st.rerun()

    # Create new project
    st.markdown("### ➕ Or create a new project")
    new_name = st.text_input("New project name")
    if st.button("📁 Create New Project") and new_name:
        new_id = create_new_project(username, new_name)
        st.session_state["project_id"] = new_id
        st.success(f"✅ New project created: {new_name}")
        st.rerun()
