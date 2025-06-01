import streamlit as st
from data_input.nodes_sql import fetch_nodes_from_db
from data_input.loads_sql import save_load_to_db, fetch_loads_from_db

def render_load_input():
    st.title("🎯 Load Input")

    # ✅ Load nodes
    nodes = fetch_nodes_from_db()
    if not nodes:
        st.warning("Please enter nodes before adding loads.")
        st.stop()

    node_options = {f"Node {n[0]}: ({n[1]}, {n[2]}, {n[3]})": n[0] for n in nodes}
    selected_label = st.selectbox("Select Node for Load", options=list(node_options.keys()))
    selected_node_id = node_options[selected_label]

    # 🎯 Force inputs
    col1, col2, col3 = st.columns(3)
    with col1:
        fx = st.number_input("Force X (Fx)", value=0.0)
    with col2:
        fy = st.number_input("Force Y (Fy)", value=0.0)
    with col3:
        fz = st.number_input("Force Z (Fz)", value=0.0)

    if st.button("➕ Add / Update Load"):
        if save_load_to_db(selected_node_id, fx, fy, fz):
            st.success(f"✅ Load saved for Node {selected_node_id}")
        else:
            st.error("❌ Failed to save load.")

    # 📋 Show saved loads
    st.subheader("📋 Saved Loads from Database:")
    loads = fetch_loads_from_db()
    if not loads:
        st.info("No loads defined yet.")
    else:
        for load in loads:
            load_id, node_id, x, y, z, fx, fy, fz = load
            st.write(
                f"Load {load_id} → Node {node_id} at ({x}, {y}, {z}) | "
                f"Fx: {fx}, Fy: {fy}, Fz: {fz}"
            )
