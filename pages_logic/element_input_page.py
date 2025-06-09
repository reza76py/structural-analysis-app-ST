import streamlit as st
from data_input.nodes_sql import fetch_nodes_from_db
from data_input.elements_sql import save_element_to_db, fetch_elements_from_db

def render_element_input():
    st.title("🧩 Element Input")

    # ✅ Ensure user is in a project
    project_id = st.session_state.get("project_id")
    if not project_id:
        st.error("❌ No project selected.")
        st.stop()

    # ✅ Load nodes from MySQL (for this project only)
    nodes = fetch_nodes_from_db(project_id)

    if len(nodes) < 2:
        st.warning("Please enter at least 2 nodes before defining elements.")
        st.stop()

    # nodes = [(id, x, y, z), ...]
    node_options = {f"Node {n[0]}: ({n[1]}, {n[2]}, {n[3]})": n[0] for n in nodes}

    # Select Start Node
    start_label = st.selectbox("Start Node", options=list(node_options.keys()), key="start_node")
    start_id = node_options[start_label]

    # Filter out start node from end options
    end_options = {label: node_id for label, node_id in node_options.items() if node_id != start_id}

    # Select End Node
    end_label = st.selectbox("End Node", options=list(end_options.keys()), key="end_node")
    end_id = end_options[end_label]

    # 💾 Save Element
    if st.button("➕ Add Element"):
        if start_id == end_id:
            st.warning("Start and end nodes must be different.")
        elif save_element_to_db(project_id, start_id, end_id):
            st.success(f"✅ Element added: Node {start_id} → Node {end_id}")
        else:
            st.warning("⚠️ Element (or reverse) already exists!")

    # 📋 Display existing elements for the current project
    st.subheader("📋 Current Elements (from MySQL):")
    elements = fetch_elements_from_db(project_id)
    if not elements:
        st.info("No elements defined yet.")
    else:
        for elem in elements:  # elem = (id, start_node_id, end_node_id)
            st.write(f"Element {elem[0]}: Node {elem[1]} → Node {elem[2]}")
