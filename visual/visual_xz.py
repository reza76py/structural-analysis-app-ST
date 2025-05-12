import plotly.graph_objects as go
import numpy as np

def plot_space_truss_xz(nodes):
    if not nodes:
        return go.Figure().update_layout(title="No nodes provided.")

    nodes = np.array(nodes)

    elements = [
        [0, 1], [1, 2], [2, 0]
    ] if len(nodes) >= 3 else []

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=nodes[:, 0],
        y=nodes[:, 2],
        mode='markers+text',
        marker=dict(size=6, color='blue'),
        text=["N{}".format(i+1) for i in range(len(nodes))],
        textposition="top center"
    ))

    for element in elements:
        start = nodes[element[0]]
        end = nodes[element[1]]
        fig.add_trace(go.Scatter(
            x=[start[0], end[0]],
            y=[start[2], end[2]],
            mode='lines',
            line=dict(color='red', width=4)
        ))

    fig.update_layout(
        title='2D Space Truss Visualization (XZ Plane)',
        xaxis_title='X Axis',
        yaxis_title='Z Axis',
        showlegend=False
    )

    return fig
