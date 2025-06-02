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

    # 🎯 New Input Style: Magnitude + Direction (angles)
    col1, col2 = st.columns(2)
    with col1:
        magnitude = st.number_input("Magnitude (N)", min_value=0.0, value=100.0)
    with col2:
        st.caption("Direction angles in degrees (relative to X, Y, Z axes)")

    colx, coly, colz = st.columns(3)
    with colx:
        theta_x = st.number_input("θₓ (deg)", value=0.0)
    with coly:
        theta_y = st.number_input("θᵧ (deg)", value=90.0)
    with colz:
        theta_z = st.number_input("θ𝓏 (deg)", value=90.0)

    if st.button("➕ Add / Update Load"):
        if save_load_to_db(selected_node_id, magnitude, theta_x, theta_y, theta_z):
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
            load_id, node_id, x, y, z, mag, tx, ty, tz = load
            st.write(
                f"Load {load_id} → Node {node_id} at ({x}, {y}, {z}) | "
                f"Magnitude: {mag} N | θₓ: {tx}°, θᵧ: {ty}°, θ𝓏: {tz}°"
            )
