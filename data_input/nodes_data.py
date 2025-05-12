import streamlit as st

def init_nodes():
    """Initialize the nodes list in session state."""
    if "nodes" not in st.session_state:
        st.session_state.nodes = []

def add_node(x, y, z):
    """Add a new node to session state."""
    st.session_state.nodes.append([x, y, z])

def get_nodes():
    """Get the current list of nodes."""
    return st.session_state.get("nodes", [])

def clear_nodes():
    """Clear all saved nodes."""
    st.session_state["nodes"] = []
