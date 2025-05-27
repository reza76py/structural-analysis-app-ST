# data_input/elements_sql.py
from data_input.db import get_connection
from mysql.connector import Error

def save_element_to_db(start_node, end_node):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # Check if reverse element exists too (2→3 vs 3→2)
        cursor.execute("""
            SELECT id FROM elements 
            WHERE (start_node = %s AND end_node = %s)
            OR (start_node = %s AND end_node = %s)
        """, (start_node, end_node, end_node, start_node))
        
        if cursor.fetchone() is None:
            cursor.execute("""
                INSERT INTO elements (start_node, end_node) 
                VALUES (%s, %s)
            """, (start_node, end_node))
            conn.commit()
            return True
        return False  # Element exists
    except Error as e:
        print(f"Error saving element: {e}")
        return False

def fetch_elements_from_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, start_node, end_node FROM elements")  # Include id
        return cursor.fetchall()
    except Error as e:
        print(f"Error fetching elements: {e}")
        return []
    

def add_element_to_db(start_node, end_node):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # Check if element exists first
        cursor.execute("SELECT id FROM elements WHERE start_node = %s AND end_node = %s", 
                      (start_node, end_node))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO elements (start_node, end_node) VALUES (%s, %s)",
                          (start_node, end_node))
            conn.commit()
            return True
        return False  # Element already exists
    except Error as e:
        print(f"Error adding element: {e}")
        return False    

