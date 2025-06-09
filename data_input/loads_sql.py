from data_input.db import get_connection
from mysql.connector import Error

def save_load_to_db(project_id, node_id, magnitude, theta_x, theta_y, theta_z):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Check if a load already exists for this node in this project
        cursor.execute("""
            SELECT id FROM loads 
            WHERE project_id = %s AND node_id = %s
        """, (project_id, node_id))
        existing = cursor.fetchone()

        if existing:
            # Update existing load
            cursor.execute("""
                UPDATE loads
                SET magnitude = %s, theta_x = %s, theta_y = %s, theta_z = %s
                WHERE project_id = %s AND node_id = %s
            """, (magnitude, theta_x, theta_y, theta_z, project_id, node_id))
        else:
            # Insert new load
            cursor.execute("""
                INSERT INTO loads (project_id, node_id, magnitude, theta_x, theta_y, theta_z)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (project_id, node_id, magnitude, theta_x, theta_y, theta_z))

        conn.commit()
        return True
    except Error as e:
        print(f"Error saving load: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def fetch_loads_from_db(project_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT l.id, n.id, n.x, n.y, n.z, l.magnitude, l.theta_x, l.theta_y, l.theta_z
            FROM loads l
            JOIN nodes n ON l.node_id = n.id
            WHERE l.project_id = %s
        """, (project_id,))
        return cursor.fetchall()
    except Error as e:
        print(f"Error fetching loads: {e}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
