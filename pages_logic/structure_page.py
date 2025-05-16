import streamlit as st
from visual.visual_xyz import plot_space_truss
from visual.visual_xy import plot_space_truss_xy
from visual.visual_xz import plot_space_truss_xz
from visual.visual_yz import plot_space_truss_yz

from data_input.nodes_sql import fetch_nodes_from_db
from data_input.elements_sql import fetch_elements_from_db

def render_structure_view():
    st.title("🏗️ Structure Visualization")

    # ✅ Load data from MySQL
    nodes = fetch_nodes_from_db()
    elements = fetch_elements_from_db()

    view_option = st.sidebar.radio("Choose view:", ["3D", "2D_xy", "2D_xz", "2D_yz"], key="view_option")

    if view_option == "3D":
        fig = plot_space_truss(nodes, elements)
    elif view_option == "2D_xy":
        fig = plot_space_truss_xy(nodes, elements)
    elif view_option == "2D_xz":
        fig = plot_space_truss_xz(nodes, elements)
    elif view_option == "2D_yz":
        fig = plot_space_truss_yz(nodes, elements)

    st.plotly_chart(fig)
