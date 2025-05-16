import plotly.graph_objects as go

def plot_space_truss(nodes, elements):
    if not nodes:
        return go.Figure().update_layout(title="⚠️ No nodes provided.")

    # Map node IDs to coordinates
    id_to_coord = {node_id: (x, y, z) for node_id, x, y, z in nodes}

    fig = go.Figure()

    # Plot nodes
    fig.add_trace(go.Scatter3d(
        x=[x for (_, x, _, _) in nodes],
        y=[y for (_, _, y, _) in nodes],
        z=[z for (_, _, _, z) in nodes],
        mode='markers+text',
        marker=dict(size=6, color='blue'),
        text=[f"N{node_id}" for (node_id, _, _, _) in nodes],
        textposition="top center"
    ))

    # Plot elements
    for start_id, end_id in elements:
        start = id_to_coord.get(start_id)
        end = id_to_coord.get(end_id)

        if start and end:
            fig.add_trace(go.Scatter3d(
                x=[start[0], end[0]],
                y=[start[1], end[1]],
                z=[start[2], end[2]],
                mode='lines',
                line=dict(color='red', width=4)
            ))

    # Camera eye positioned to make Z-axis come toward the viewer (math right-hand rule)
    fig.update_layout(
        scene=dict(
            xaxis_title='X Axis',
            yaxis_title='Y Axis',
            zaxis_title='Z Axis',
            aspectmode='cube',
            camera=dict(
                eye=dict(x=-1.5, y=-1.5, z=1)  # Lower z means looking more down the Z-axis
            )
        ),
        title="🧱 3D Truss View (Math Right-Hand Rule)",
        showlegend=False
    )

    return fig
