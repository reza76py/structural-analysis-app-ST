from data_input.db import get_connection
from mysql.connector import Error

def save_support_to_db(project_id, node_id, x_restrained, y_restrained, z_restrained):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Check if support for the node in the project already exists
        cursor.execute("""
            SELECT id FROM supports 
            WHERE project_id = %s AND node_id = %s
        """, (project_id, node_id))
        existing = cursor.fetchone()

        if existing:
            # Update existing support
            cursor.execute("""
                UPDATE supports 
                SET x_restrained = %s, y_restrained = %s, z_restrained = %s 
                WHERE project_id = %s AND node_id = %s
            """, (x_restrained, y_restrained, z_restrained, project_id, node_id))
        else:
            # Insert new support
            cursor.execute("""
                INSERT INTO supports (project_id, node_id, x_restrained, y_restrained, z_restrained)
                VALUES (%s, %s, %s, %s, %s)
            """, (project_id, node_id, x_restrained, y_restrained, z_restrained))

        conn.commit()
        return True
    except Error as e:
        print(f"Error saving support: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def fetch_supports_from_db(project_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.id, n.id, n.x, n.y, n.z, s.x_restrained, s.y_restrained, s.z_restrained
            FROM supports s
            JOIN nodes n ON s.node_id = n.id
            WHERE s.project_id = %s
        """, (project_id,))
        return cursor.fetchall()
    except Error as e:
        print(f"Error fetching supports: {e}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
