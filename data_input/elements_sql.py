# data_input/elements_sql.py

from data_input.db import get_connection

def save_element_to_db(start_node_id, end_node_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO elements (start_node_id, end_node_id)
        VALUES (%s, %s)
    """
    cursor.execute(query, (start_node_id, end_node_id))
    conn.commit()
    conn.close()

def fetch_elements_from_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT start_node, end_node FROM elements")
    elements = cursor.fetchall()
    conn.close()
    return elements
