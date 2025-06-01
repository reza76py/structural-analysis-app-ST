from data_input.db import get_connection
from mysql.connector import Error

def save_support_to_db(node_id, x_restrained, y_restrained, z_restrained):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Check if support for the node already exists
        cursor.execute("SELECT id FROM supports WHERE node_id = %s", (node_id,))
        existing = cursor.fetchone()

        if existing:
            # Update existing support
            cursor.execute("""
                UPDATE supports 
                SET x_restrained = %s, y_restrained = %s, z_restrained = %s 
                WHERE node_id = %s
            """, (x_restrained, y_restrained, z_restrained, node_id))
        else:
            # Insert new support
            cursor.execute("""
                INSERT INTO supports (node_id, x_restrained, y_restrained, z_restrained)
                VALUES (%s, %s, %s, %s)
            """, (node_id, x_restrained, y_restrained, z_restrained))

        conn.commit()
        return True
    except Error as e:
        print(f"Error saving support: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def fetch_supports_from_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.id, n.id, n.x, n.y, n.z, s.x_restrained, s.y_restrained, s.z_restrained
            FROM supports s
            JOIN nodes n ON s.node_id = n.id
        """)
        return cursor.fetchall()
    except Error as e:
        print(f"Error fetching supports: {e}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
