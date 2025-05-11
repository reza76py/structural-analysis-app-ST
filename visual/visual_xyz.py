import plotly.graph_objects as go
import numpy as np


def plot_space_truss(nodes):


    # Define elements (connections between nodes)
    elements = [
        [0, 1], [1, 2], [2, 0],    # Base triangle
    ]

    # Create a Plotly figure
    fig = go.Figure()

    # Plot the nodes as scatter points
    fig.add_trace(go.Scatter3d(
        x=nodes[:, 0],
        y=nodes[:, 1],
        z=nodes[:, 2],
        mode='markers+text+lines',
        marker=dict(size=6, color='blue'),
        text=["N{}".format(i+1) for i in range(len(nodes))],
        textposition="top center",
        texttemplate='%{text}(%{x},%{y},%{z})'  # Customize text to include coordinates
    ))




    # Plot the elements (truss members) as lines connecting the nodes
    for element in elements:
        node_start = nodes[element[0]]
        node_end = nodes[element[1]]
        
        fig.add_trace(go.Scatter3d(
            x=[node_start[0], node_end[0]],
            y=[node_start[1], node_end[1]],
            z=[node_start[2], node_end[2]],
            mode='lines',
            line=dict(color='red', width=4)
        ))

    # Customize the layout for better appearance
    fig.update_layout(

        scene=dict(
            xaxis_title='X Axis',
            yaxis_title='Y Axis',
            zaxis_title='Z Axis',
            aspectmode='cube',  # Ensure the axes are equally scaled
            xaxis=dict(range=[-2, 12]),
            yaxis=dict(range=[-2, 12]),
            zaxis=dict(range=[-2, 12]),
        ),
        showlegend=False
    )

    return fig
