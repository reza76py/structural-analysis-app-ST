import plotly.graph_objects as go
import numpy as np

def plot_space_truss_yz(nodes):

    # Define elements (connections between nodes)
    elements = [
        [0, 1], [1, 2], [2, 0],    # Base triangle
    ]

    # Create a Plotly figure for the YZ view
    fig = go.Figure()

    # Plot the nodes as scatter points (YZ view)
    fig.add_trace(go.Scatter(
        x=nodes[:, 1],  # Y values
        y=nodes[:, 2],  # Z values
        mode='markers+text',
        marker=dict(size=6, color='blue'),
        text=["N{}".format(i+1) for i in range(len(nodes))],
        textposition="top center",
    ))

    # Plot the elements (truss members) as lines connecting the nodes (YZ view)
    for element in elements:
        node_start = nodes[element[0]]
        node_end = nodes[element[1]]
        
        fig.add_trace(go.Scatter(
            x=[node_start[1], node_end[1]],
            y=[node_start[2], node_end[2]],
            mode='lines',
            line=dict(color='red', width=4)
        ))

    fig.update_layout(
        title='2D Space Truss Visualization (YZ Plane)',
        xaxis_title='Y Axis',
        yaxis_title='Z Axis',
        showlegend=False
    )

    return fig
