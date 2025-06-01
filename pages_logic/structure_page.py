import streamlit as st
from visual.visual_xyz import plot_space_truss
from visual.visual_xy import plot_space_truss_xy
from visual.visual_xz import plot_space_truss_xz
from visual.visual_yz import plot_space_truss_yz

from data_input.nodes_sql import fetch_nodes_from_db
from data_input.elements_sql import fetch_elements_from_db
from data_input.supports_sql import fetch_supports_from_db


def render_structure_view():
    st.title("🏗️ Structure Visualization")

    # ✅ Load data from MySQL
    nodes = fetch_nodes_from_db()
    elements = fetch_elements_from_db()
    supports = fetch_supports_from_db()


    # ✅ View selection
    view_option = st.sidebar.radio("Choose view:", ["3D", "2D_xy", "2D_xz", "2D_yz"], key="view_option")

    # ✅ Initialize section filter variables
    filter_mode = None
    section_value = None

    # ✅ Show section filter controls depending on view
    if view_option == "2D_xy":
        st.sidebar.markdown("### Z-Section Filter")
        enable_filter = st.sidebar.checkbox("Enable Z Filter", value=False)
        if enable_filter:
            section_value = st.sidebar.number_input("Z value to filter by", value=0)
            filter_mode = st.sidebar.selectbox("Z Filter Mode", ["==", "<=", ">="])
    elif view_option == "2D_xz":
        st.sidebar.markdown("### Y-Section Filter")
        enable_filter = st.sidebar.checkbox("Enable Y Filter", value=False)
        if enable_filter:
            section_value = st.sidebar.number_input("Y value to filter by", value=0)
            filter_mode = st.sidebar.selectbox("Y Filter Mode", ["==", "<=", ">="])
    elif view_option == "2D_yz":
        st.sidebar.markdown("### X-Section Filter")
        enable_filter = st.sidebar.checkbox("Enable X Filter", value=False)
        if enable_filter:
            section_value = st.sidebar.number_input("X value to filter by", value=0)
            filter_mode = st.sidebar.selectbox("X Filter Mode", ["==", "<=", ">="])

    # ✅ Plot based on view
    if view_option == "3D":
        fig = plot_space_truss(nodes, elements, supports)
    elif view_option == "2D_xy":
        fig = plot_space_truss_xy(
            nodes, elements,
            z_section=section_value if filter_mode else None,
            filter_mode=filter_mode
        )
    elif view_option == "2D_xz":
        fig = plot_space_truss_xz(
            nodes, elements,
            y_section=section_value if filter_mode else None,
            filter_mode=filter_mode
        )
    elif view_option == "2D_yz":
        fig = plot_space_truss_yz(
            nodes, elements,
            x_section=section_value if filter_mode else None,
            filter_mode=filter_mode
        )

    st.plotly_chart(fig)
