import streamlit as st
from data_input.nodes_sql import fetch_nodes_from_db
from data_input.supports_sql import save_support_to_db, fetch_supports_from_db

def render_support_input():
    st.title("🧱 Support Input")

    # ✅ Fetch nodes
    nodes = fetch_nodes_from_db()
    if not nodes:
        st.warning("Please enter nodes before assigning supports.")
        st.stop()

    # 🧩 Prepare node dropdown
    node_options = {f"Node {n[0]}: ({n[1]}, {n[2]}, {n[3]})": n[0] for n in nodes}
    selected_label = st.selectbox("Select Node for Support", options=list(node_options.keys()))
    selected_node_id = node_options[selected_label]

    # 🎯 Checkbox inputs for DOF restraint
    col1, col2, col3 = st.columns(3)
    with col1:
        x_rest = st.checkbox("Restrained in X")
    with col2:
        y_rest = st.checkbox("Restrained in Y")
    with col3:
        z_rest = st.checkbox("Restrained in Z")

    # 💾 Save Support
    if st.button("➕ Add / Update Support"):
        if save_support_to_db(selected_node_id, x_rest, y_rest, z_rest):
            st.success(f"✅ Support saved for Node {selected_node_id}")
        else:
            st.error("❌ Failed to save support.")

    # 📋 Show current supports
    st.subheader("📋 Saved Supports from Database:")
    supports = fetch_supports_from_db()
    if not supports:
        st.info("No supports defined yet.")
    else:
        for support in supports:
            support_id, node_id, x, y, z, x_rest, y_rest, z_rest = support
            st.write(
                f"Support {support_id} → Node {node_id} at ({x}, {y}, {z}) | "
                f"X: {'🔒' if x_rest else '🟢'}, "
                f"Y: {'🔒' if y_rest else '🟢'}, "
                f"Z: {'🔒' if z_rest else '🟢'}"
            )
