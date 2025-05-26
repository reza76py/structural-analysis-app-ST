# import mysql.connector


# def get_connection():
#     try:
#         return mysql.connector.connect(
#             host="host.docker.internal",
#             user="space_truss_db_st_user",
#             password="934",
#             database="space_truss_db_st",
#             auth_plugin='caching_sha2_password',  # Add this line
#             port=3306  # Explicit port
#         )
#     except mysql.connector.Error as err:
#         print(f"Connection error: {err}")
#         raise





import os
import mysql.connector

def get_connection():
    in_docker = os.getenv("IN_DOCKER", "false").lower() == "true"
    host = "host.docker.internal" if in_docker else "localhost"
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
