import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="space_truss_db_st_user",
        password="934",
        database="space_truss_db_st"
    )