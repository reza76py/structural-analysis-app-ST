import os
import mysql.connector

def get_connection():
    in_docker = os.getenv("IN_DOCKER", "false").lower() == "true"
    host = "db" if in_docker else "localhost"  # Changed to service name
    try:
        return mysql.connector.connect(
            host=host,
            user="space_truss_db_st_user",
            password="934",
            database="space_truss_db_st",
            auth_plugin='caching_sha2_password',
            port=3306
        )
    except mysql.connector.Error as err:
        print(f"Connection error: {err}")
        raise