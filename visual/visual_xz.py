import plotly.graph_objects as go

def plot_space_truss_xz(nodes, elements):
    if not nodes:
        return go.Figure().update_layout(title="⚠️ No nodes provided.")

    # Create dictionary of node_id → (x, z)
    id_to_coord = {node_id: (x, z) for node_id, x, _, z in nodes}

    fig = go.Figure()

    # Plot nodes
    fig.add_trace(go.Scatter(
        x=[x for (_, x, _, _) in nodes],
        y=[z for (_, _, _, z) in nodes],
        mode='markers+text',
        marker=dict(size=6, color='blue'),
        text=[f"N{id}" for (id, _, _, _) in nodes],
        textposition="top center"
    ))

    # Plot elements
    for start_id, end_id in elements:
        start = id_to_coord.get(start_id)
        end = id_to_coord.get(end_id)

        if start and end:
            fig.add_trace(go.Scatter(
                x=[start[0], end[0]],
                y=[start[1], end[1]],
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
