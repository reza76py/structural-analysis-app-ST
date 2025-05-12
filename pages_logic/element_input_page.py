import streamlit as st
from data_input.elements_data import init_elements, add_element, get_elements, clear_elements

def render_element_input():
    st.title("🧩 Element Input")

    nodes = st.session_state.get("nodes", [])
    if len(nodes) < 2:
        st.warning("Please enter at least 2 nodes before defining elements.")
        st.stop()

    init_elements()
    node_labels = [f"Node {i+1}: {coord}" for i, coord in enumerate(nodes)]

    start = st.selectbox("Start Node", range(len(nodes)), format_func=lambda i: node_labels[i])
    end = st.selectbox("End Node", range(len(nodes)), format_func=lambda i: node_labels[i])

    if st.button("➕ Add Element"):
        add_element(start, end)

    st.subheader("📋 Current Elements:")
    for i, e in enumerate(get_elements()):
        st.write(f"Element {i+1}: Node {e[0]+1} → Node {e[1]+1}")

    if st.button("🗑️ Clear All Elements"):
        clear_elements()
        st.warning("All elements cleared.")
