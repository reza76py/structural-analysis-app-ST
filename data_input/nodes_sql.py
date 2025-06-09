from data_input.db import get_connection

def save_node_to_db(project_id,x, y, z):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO nodes (project_id, x, y, z) VALUES (%s, %s, %s, %s)", (project_id, x, y, z))
    conn.commit()
    conn.close()

def fetch_nodes_from_db(project_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, x, y, z FROM nodes WHERE project_id = %s", (project_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows
