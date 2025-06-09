import os
os.environ["STREAMLIT_SERVER_BASE_URL_PATH"] = "/space-truss"

import streamlit as st
from auth.login import check_login
from auth.session import is_logged_in, logout_button
from auth.project_selector import render_project_selector

# Page components
from pages_logic.node_input_page import render_node_input
from pages_logic.element_input_page import render_element_input
from pages_logic.structure_page import render_structure_view
from pages_logic.support_input_page import render_support_input
from pages_logic.load_input_page import render_load_input

# App settings
st.set_page_config(page_title="Space Truss App", layout="wide", page_icon="🧮")

# ⛔ Block access if not logged in
if not check_login():
    st.stop()

# ✅ Show logout in sidebar
logout_button()

# ✅ Require project selection after login
if "project_id" not in st.session_state:
    render_project_selector()
    st.stop()

# 🧭 Sidebar menu
st.sidebar.title("Space Truss Menu")
selectbox_page = st.sidebar.selectbox(
    "Navigate to",
    ["Nodes Input", "Element Input", "Supports Input", "Loads Input", "Structure"]
)

# 🚀 Page routing
if selectbox_page == "Nodes Input":
    render_node_input()
elif selectbox_page == "Element Input":
    render_element_input()
elif selectbox_page == "Supports Input":
    render_support_input()
elif selectbox_page == "Loads Input":
    render_load_input()
elif selectbox_page == "Structure":
    render_structure_view()
