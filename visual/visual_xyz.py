import plotly.graph_objects as go

def plot_space_truss(nodes, elements):
    if not nodes:
        return go.Figure().update_layout(title="⚠️ No nodes provided")

    # Map node_id to (x, y, z) coordinates
    id_to_coord = {node[0]: node[1:] for node in nodes}  # {id: (x, y, z)}

    fig = go.Figure()

    # Plot nodes
    node_x, node_y, node_z, node_ids = zip(*[(x, y, z, id) for id, x, y, z in nodes])
    fig.add_trace(go.Scatter3d(
        x=node_x,
        y=node_y,
        z=node_z,
        mode='markers+text',
        marker=dict(size=6, color='blue'),
        text=[f"N{id}" for id in node_ids],
        textposition="top center",
        name="Nodes"
    ))

    # Plot elements
    for elem_id, (_, start_id, end_id) in enumerate(elements, 1):
        start = id_to_coord.get(start_id)
        end = id_to_coord.get(end_id)

        if start and end:
            fig.add_trace(go.Scatter3d(
                x=[start[0], end[0]],
                y=[start[1], end[1]],
                z=[start[2], end[2]],
                mode='lines',
                line=dict(color='red', width=4),
                name=f"Element {elem_id}",
                hoverinfo='text',
                hovertext=f"<b>Element:</b> Node {start_id} → Node {end_id}",
                showlegend=False
            ))

    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode='data',
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=0.8),
                up=dict(x=0, y=0, z=1)
            )
        ),
        title="3D Truss Visualization",
        margin=dict(l=0, r=0, b=0, t=30)
    )

    return fig
