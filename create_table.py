import db_conn
from db_conn import conn
from dotenv import load_dotenv
import os
load_dotenv()
table_name=os.getenv('table_name')
def create_table(conn):
    try:
        cursor=conn.cursor()
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL
            )
            """
        )
        cursor.close()
        print(f"Table '{table_name}' created successfully")
    except Exception as e:
         print(f"Error creating table '{table_name}': {e}")

create_table(conn)         