import plotly.graph_objects as go

def plot_space_truss(nodes, elements, supports=[], loads=[]):
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

    # 🟡 Plot support arrows and center dots
    arrow_len = 1.5  # arrow length

    for support in supports:
        _, node_id, x, y, z, x_rest, y_rest, z_rest = support

        # ⚫ Base dot at support node (for tidiness)
        if x_rest or y_rest or z_rest:
            fig.add_trace(go.Scatter3d(
                x=[x],
                y=[y],
                z=[z],
                mode='markers',
                marker=dict(size=4, color='black'),
                showlegend=False,
                hoverinfo='skip'
            ))

        # X-direction arrow (←)
        if x_rest:
            fig.add_trace(go.Scatter3d(
                x=[x - 0.5*arrow_len, x + 0.5*arrow_len],
                y=[y, y],
                z=[z, z],
                mode='lines',
                line=dict(color='red', width=15, dash='dot'),
                opacity=0.8,
                showlegend=False,
                hoverinfo='text',
                hovertext=f"🔒 X-restrained at Node {node_id}"
            ))

        # Y-direction arrow (↓)
        if y_rest:
            fig.add_trace(go.Scatter3d(
                x=[x, x],
                y=[y - 0.5*arrow_len, y + 0.5*arrow_len],
                z=[z, z],
                mode='lines',
                line=dict(color='green', width=15, dash='dot'),
                opacity=0.8,
                showlegend=False,
                hoverinfo='text',
                hovertext=f"🔒 Y-restrained at Node {node_id}"
            ))

        # Z-direction arrow (↓)
        if z_rest:
            fig.add_trace(go.Scatter3d(
                x=[x, x],
                y=[y, y],
                z=[z - 0.5*arrow_len, z + 0.5*arrow_len],
                mode='lines',
                line=dict(color='blue', width=15, dash='dot'),
                opacity=0.8,
                showlegend=False,
                hoverinfo='text',
                hovertext=f"🔒 Z-restrained at Node {node_id}"
            ))


        scale = 0.2  # Increased for visibility

    # 🟠 Loads
    scale = 0.2
    for load in loads:
        _, node_id, x, y, z, fx, fy, fz = load
        if fx != 0:
            fig.add_trace(go.Scatter3d(
                x=[x, x + fx * scale], y=[y, y], z=[z, z],
                mode='lines',
                line=dict(color='red', width=3),
                showlegend=False,
                hoverinfo='text',
                hovertext=f"Fx = {fx} at Node {node_id}"
            ))
            fig.add_trace(go.Scatter3d(
                x=[x], y=[y], z=[z],
                mode='markers',
                marker=dict(size=3, color='red'),
                showlegend=False,
                hoverinfo='skip'
            ))
        if fy != 0:
            fig.add_trace(go.Scatter3d(
                x=[x, x], y=[y, y + fy * scale], z=[z, z],
                mode='lines',
                line=dict(color='green', width=3),
                showlegend=False,
                hoverinfo='text',
                hovertext=f"Fy = {fy} at Node {node_id}"
            ))
            fig.add_trace(go.Scatter3d(
                x=[x], y=[y], z=[z],
                mode='markers',
                marker=dict(size=3, color='green'),
                showlegend=False,
                hoverinfo='skip'
            ))
        if fz != 0:
            fig.add_trace(go.Scatter3d(
                x=[x, x], y=[y, y], z=[z, z + fz * scale],
                mode='lines',
                line=dict(color='blue', width=3),
                showlegend=False,
                hoverinfo='text',
                hovertext=f"Fz = {fz} at Node {node_id}"
            ))
            fig.add_trace(go.Scatter3d(
                x=[x], y=[y], z=[z],
                mode='markers',
                marker=dict(size=3, color='blue'),
                showlegend=False,
                hoverinfo='skip'
            ))
        

    # 📐 Layout settings
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