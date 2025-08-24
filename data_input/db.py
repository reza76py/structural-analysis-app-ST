# import os
# import mysql.connector

# def get_connection():
#     in_docker = os.getenv("IN_DOCKER", "false").lower() == "true"
#     host = "db" if in_docker else "localhost"  # Changed to service name
#     try:
#         return mysql.connector.connect(
#             host=host,
#             user="space_truss_db_st_user",
#             password="934",
#             database="space_truss_db_st",
#             auth_plugin='caching_sha2_password',
#             port=3306
#         )
#     except mysql.connector.Error as err:
#         print(f"Connection error: {err}")
#         raise










# data_input/db.py
import os
import mysql.connector

def get_connection():
    host = os.getenv("DB_HOST", "localhost")
    user = os.getenv("DB_USER", "space_truss_db_st_user")
    password = os.getenv("DB_PASSWORD", "934")  # change locally as needed
    database = os.getenv("DB_NAME", "space_truss_db_st")
    port = int(os.getenv("DB_PORT", "3306"))

    try:
        return mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port,
            auth_plugin="caching_sha2_password",
        )
    except mysql.connector.Error as err:
        print(f"Connection error: {err}")
        raise
