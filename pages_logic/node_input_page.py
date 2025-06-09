import streamlit as st
from data_input.nodes_sql import save_node_to_db, fetch_nodes_from_db

def render_node_input():
    st.title("🧮 Node Input")

    col1, col2, col3 = st.columns(3)

    with col1:
        x_input = st.text_input("X", value="0")
    with col2:
        y_input = st.text_input("Y", value="0")
    with col3:
        z_input = st.text_input("Z", value="0")

    try:
        x = int(x_input)
        y = int(y_input)
        z = int(z_input)
    except ValueError:
        st.error("❌ Please enter valid integers.")
        st.stop()

    if st.button("➕ Add Node"):
        save_node_to_db(st.session_state["project_id"], x, y, z)

        st.success(f"✅ Node saved to MySQL: ({x}, {y}, {z})")

    st.subheader("📋 Saved Nodes from Database:")
    nodes = nodes = fetch_nodes_from_db(st.session_state["project_id"])

    for node in nodes:
        st.write(f"Node {node[0]}: (X={node[1]}, Y={node[2]}, Z={node[3]})")
