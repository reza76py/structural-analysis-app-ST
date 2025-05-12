import plotly.graph_objects as go
import numpy as np

def plot_space_truss(nodes, elements):
    if not nodes:
        return go.Figure().update_layout(title="No nodes provided.")
    
    nodes = np.array(nodes)

    fig = go.Figure()

    # Plot nodes
    fig.add_trace(go.Scatter3d(
        x=nodes[:, 0],
        y=nodes[:, 1],
        z=nodes[:, 2],
        mode='markers+text',
        marker=dict(size=6, color='blue'),
        text=[f"N{i+1}" for i in range(len(nodes))],
        textposition="top center"
    ))

    # Plot elements if available
    if elements:
        for element in elements:
            start = nodes[element[0]]
            end = nodes[element[1]]

            fig.add_trace(go.Scatter3d(
                x=[start[0], end[0]],
                y=[start[1], end[1]],
                z=[start[2], end[2]],
                mode='lines',
                line=dict(color='red', width=4)
            ))

    fig.update_layout(
        scene=dict(
            xaxis_title='X Axis',
            yaxis_title='Y Axis',
            zaxis_title='Z Axis',
            aspectmode='cube'
        ),
        title="3D Truss View",
        showlegend=False
    )

    return fig
