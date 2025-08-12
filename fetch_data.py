import db_conn
from db_conn import conn
from dotenv import load_dotenv
import os

load_dotenv()

table_name = os.getenv('table_name')
db_name = os.getenv('db_name')


def fetch_data(conn):
    try:
        cursor=conn.cursor()
        cursor.execute(f"USE {db_name}")
        cursor.execute(f"SELECT name FROM {table_name}")
        rows = cursor.fetchall()
        if not rows:
            return []
        print(f"Data fetched successfully from '{table_name}': {rows}")
        return rows
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
    finally:
        cursor.close()
        conn.close()
fetch_data(conn)