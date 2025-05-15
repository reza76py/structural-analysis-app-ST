from data_input.db import get_connection

def save_node_to_db(x, y, z):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO nodes (x, y, z) VALUES (%s, %s, %s)", (x, y, z))
    conn.commit()
    conn.close()

def fetch_nodes_from_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, x, y, z FROM nodes")
    rows = cursor.fetchall()
    conn.close()
    return rows
