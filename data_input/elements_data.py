import streamlit as st

def init_elements():
    """Initialize elements list in session state."""
    if "elements" not in st.session_state:
        st.session_state.elements = []

def add_element(start_index, end_index):
    """Add a new element if it’s valid and not duplicated."""
    new_element = [start_index, end_index]
    reversed_element = [end_index, start_index]

    if start_index == end_index:
        st.warning("Start and end nodes must be different.")
        return

    if new_element in st.session_state.elements or reversed_element in st.session_state.elements:
        st.info("This element already exists.")
        return

    st.session_state.elements.append(new_element)

def get_elements():
    """Get the list of elements."""
    return st.session_state.get("elements", [])

def clear_elements():
    """Clear all elements."""
    st.session_state["elements"] = []
