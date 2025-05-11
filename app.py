import streamlit as st
from data_input.nodes_data import read_nodes_from_excel
from visual.visual_xyz import plot_space_truss  # Import the function
from visual.visual_xy import plot_space_truss_xy
from visual.visual_xz import plot_space_truss_xz
from visual.visual_yz import plot_space_truss_yz


# Load nodes from Excel
try:
    nodes = read_nodes_from_excel()
except Exception as e:
    st.error(f"Failed to load nodes: {e}")
    st.stop()


# Create a button to switch between views
view = st.radio(
    "Choose the view",
    ("3D View", "XY View", "XZ View", "YZ View")
)

if view == "3D View":
    fig = plot_space_truss(nodes)
elif view == "XY View":
    fig = plot_space_truss_xy(nodes)
elif view == "XZ View":
    fig = plot_space_truss_xz(nodes)    

elif view == "YZ View":
    fig = plot_space_truss_yz(nodes)    

# Display the selected plot in Streamlit
st.plotly_chart(fig)