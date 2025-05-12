import streamlit as st
from visual.visual_xyz import plot_space_truss
from visual.visual_xy import plot_space_truss_xy
from visual.visual_xz import plot_space_truss_xz
from visual.visual_yz import plot_space_truss_yz

def render_structure_view():
    st.title("🏗️ Structure Visualization")

    nodes = st.session_state.get("nodes", [])
    elements = st.session_state.get("elements", [])

    view_option = st.sidebar.radio("Choose view:", ["3D", "2D_xy", "2D_xz", "2D_yz"], key="view_option")

    if view_option == "3D":
        fig = plot_space_truss(nodes, elements)
    elif view_option == "2D_xy":
        fig = plot_space_truss_xy(nodes)
    elif view_option == "2D_xz":
        fig = plot_space_truss_xz(nodes)
    elif view_option == "2D_yz":
        fig = plot_space_truss_yz(nodes)

    st.plotly_chart(fig)

