import streamlit as st
from data_input.nodes_data import init_nodes, add_node, get_nodes, clear_nodes

def render_node_input():
    st.title("🧮 Node Input")
    
    init_nodes()

    x = st.number_input("X Coordinate")
    y = st.number_input("Y Coordinate")
    z = st.number_input("Z Coordinate")

    if st.button("➕ Add Node"):
        add_node(x, y, z)
        st.success(f"Node added: ({x}, {y}, {z})")

    st.subheader("📋 Current Nodes:")
    for i, node in enumerate(get_nodes()):
        st.write(f"Node {i+1}: {node}")

    if st.button("🗑️ Clear Nodes"):
        clear_nodes()
        st.warning("All nodes cleared.")
