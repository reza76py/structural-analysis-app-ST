from data_input.db import get_connection
from mysql.connector import Error

def save_load_to_db(node_id, magnitude, theta_x, theta_y, theta_z):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Check if a load already exists for this node
        cursor.execute("SELECT id FROM loads WHERE node_id = %s", (node_id,))
        existing = cursor.fetchone()

        if existing:
            # Update existing load
            cursor.execute("""
                UPDATE loads
                SET magnitude = %s, theta_x = %s, theta_y = %s, theta_z = %s
                WHERE node_id = %s
            """, (magnitude, theta_x, theta_y, theta_z, node_id))
        else:
            # Insert new load
            cursor.execute("""
                INSERT INTO loads (node_id, magnitude, theta_x, theta_y, theta_z)
                VALUES (%s, %s, %s, %s, %s)
            """, (node_id, magnitude, theta_x, theta_y, theta_z))

        conn.commit()
        return True
    except Error as e:
        print(f"Error saving load: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def fetch_loads_from_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT l.id, n.id, n.x, n.y, n.z, l.magnitude, l.theta_x, l.theta_y, l.theta_z
            FROM loads l
            JOIN nodes n ON l.node_id = n.id
        """)
        return cursor.fetchall()
    except Error as e:
        print(f"Error fetching loads: {e}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()