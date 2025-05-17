import plotly.graph_objects as go

def plot_space_truss_yz(nodes, elements, x_section=None, filter_mode=None):
    if not nodes:
        return go.Figure().update_layout(title="⚠️ No nodes provided.")

    filtered_nodes = []
    unfiltered_nodes = []

    if x_section is not None and filter_mode in ["==", "<=", ">="]:
        for node in nodes:
            node_id, x, y, z = node
            if (
                (filter_mode == "==" and x == x_section) or
                (filter_mode == "<=" and x <= x_section) or
                (filter_mode == ">=" and x >= x_section)
            ):
                filtered_nodes.append(node)
            else:
                unfiltered_nodes.append(node)
    else:
        filtered_nodes = nodes

    filtered_node_ids = set(n[0] for n in filtered_nodes)
    id_to_coord = {node_id: (y, z) for node_id, _, y, z in nodes}

    fig = go.Figure()

    if unfiltered_nodes:
        fig.add_trace(go.Scatter(
            x=[y for (_, _, y, _) in unfiltered_nodes],
            y=[z for (_, _, _, z) in unfiltered_nodes],
            mode='markers+text',
            marker=dict(size=6, color='lightgray'),
            text=[f"N{id}" for (id, _, _, _) in unfiltered_nodes],
            textposition="top center",
            name="Unfiltered Nodes"
        ))

    if filtered_nodes:
        fig.add_trace(go.Scatter(
            x=[y for (_, _, y, _) in filtered_nodes],
            y=[z for (_, _, _, z) in filtered_nodes],
            mode='markers+text',
            marker=dict(size=6, color='blue'),
            text=[f"N{id}" for (id, _, _, _) in filtered_nodes],
            textposition="top center",
            name="Filtered Nodes"
        ))

    for start_id, end_id in elements:
        start = id_to_coord.get(start_id)
        end = id_to_coord.get(end_id)

        if start and end:
            both_inside = start_id in filtered_node_ids and end_id in filtered_node_ids
            line_color = 'red' if both_inside else 'orange'
            line_style = 'solid' if both_inside else 'dash'
            hover_text = (
                f"<b>Element:</b> Node {start_id} → Node {end_id}<br>"
                f"<b>Start:</b> (Y={start[0]}, Z={start[1]})<br>"
                f"<b>End:</b> (Y={end[0]}, Z={end[1]})"
            )

            fig.add_trace(go.Scatter(
                x=[start[0], end[0]],
                y=[start[1], end[1]],
                mode='lines',
                line=dict(color=line_color, width=4, dash=line_style),
                name="In Filter" if both_inside else "Crosses Filter",
                hoverinfo='text',
                hovertext=hover_text
            ))

    return fig
