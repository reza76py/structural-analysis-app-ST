# from data_input.db import get_connection
# from mysql.connector import Error

# def save_element_to_db(project_id, start_node_id, end_node_id):
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()
#         # Check if reverse element exists too (e.g., 2→3 vs 3→2)
#         cursor.execute("""
#             SELECT id FROM elements 
#             WHERE project_id = %s AND (
#                 (start_node_id = %s AND end_node_id = %s) OR
#                 (start_node_id = %s AND end_node_id = %s)
#             )
#         """, (project_id, start_node_id, end_node_id, end_node_id, start_node_id))
        
#         if cursor.fetchone() is None:
#             cursor.execute("""
#                 INSERT INTO elements (project_id, start_node_id, end_node_id) 
#                 VALUES (%s, %s)
#             """, (project_id, start_node_id, end_node_id))
#             conn.commit()
#             return True
#         return False  # Element (or reverse) already exists
#     except Error as e:
#         print(f"Error saving element: {e}")
#         return False
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()

# def fetch_elements_from_db():
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()
#         cursor.execute("SELECT id, start_node_id, end_node_id FROM elements")
#         return cursor.fetchall()
#     except Error as e:
#         print(f"Error fetching elements: {e}")
#         return []
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()

# def add_element_to_db(start_node_id, end_node_id):
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()
#         cursor.execute("""
#             SELECT id FROM elements 
#             WHERE start_node_id = %s AND end_node_id = %s
#         """, (start_node_id, end_node_id))
#         if cursor.fetchone() is None:
#             cursor.execute("""
#                 INSERT INTO elements (start_node_id, end_node_id) 
#                 VALUES (%s, %s)
#             """, (start_node_id, end_node_id))
#             conn.commit()
#             return True
#         return False  # Element already exists
#     except Error as e:
#         print(f"Error adding element: {e}")
#         return False
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()











from data_input.db import get_connection
from mysql.connector import Error

def save_element_to_db(project_id, start_node_id, end_node_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # Check if element or reverse exists in the same project
        cursor.execute("""
            SELECT id FROM elements 
            WHERE project_id = %s AND (
                (start_node_id = %s AND end_node_id = %s) OR
                (start_node_id = %s AND end_node_id = %s)
            )
        """, (project_id, start_node_id, end_node_id, end_node_id, start_node_id))

        if cursor.fetchone() is None:
            cursor.execute("""
                INSERT INTO elements (project_id, start_node_id, end_node_id) 
                VALUES (%s, %s, %s)
            """, (project_id, start_node_id, end_node_id))
            conn.commit()
            return True
        return False  # Element (or reverse) already exists
    except Error as e:
        print(f"Error saving element: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def fetch_elements_from_db(project_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, start_node_id, end_node_id 
            FROM elements 
            WHERE project_id = %s
        """, (project_id,))
        return cursor.fetchall()
    except Error as e:
        print(f"Error fetching elements: {e}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def add_element_to_db(project_id, start_node_id, end_node_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id FROM elements 
            WHERE project_id = %s AND start_node_id = %s AND end_node_id = %s
        """, (project_id, start_node_id, end_node_id))
        if cursor.fetchone() is None:
            cursor.execute("""
                INSERT INTO elements (project_id, start_node_id, end_node_id) 
                VALUES (%s, %s, %s)
            """, (project_id, start_node_id, end_node_id))
            conn.commit()
            return True
        return False  # Element already exists
    except Error as e:
        print(f"Error adding element: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
