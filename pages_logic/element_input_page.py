import streamlit as st
from data_input.nodes_sql import fetch_nodes_from_db
from data_input.elements_sql import save_element_to_db, fetch_elements_from_db

def render_element_input():
    st.title("🧩 Element Input")

    # ✅ Load nodes from MySQL
    nodes = fetch_nodes_from_db()

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


    start_id = node_options[start_label]
    end_id = node_options[end_label]

    if st.button("➕ Add Element"):
        if start_id == end_id:
            st.warning("Start and end nodes must be different.")
        else:
            save_element_to_db(start_id, end_id)
            st.success(f"Element added: Node {start_id} → Node {end_id}")

    # Display from DB
    st.subheader("📋 Current Elements (from MySQL):")
    elements = fetch_elements_from_db()
    for i, (start_node, end_node) in enumerate(elements):
        st.write(f"Element {i+1}: Node {start_node} → Node {end_node}")
