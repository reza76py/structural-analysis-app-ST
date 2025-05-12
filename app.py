import streamlit as st
from pages_logic.node_input_page import render_node_input
from pages_logic.element_input_page import render_element_input
from pages_logic.structure_page import render_structure_view

st.set_page_config(page_title="Space Truss App")

st.sidebar.title("🔧 Space Truss Menu")
main_page = st.sidebar.radio("Navigate to:", ["Nodes Input", "Element Input", "Structure"])

if main_page == "Nodes Input":
    render_node_input()
elif main_page == "Element Input":
    render_element_input()
elif main_page == "Structure":
    render_structure_view()
