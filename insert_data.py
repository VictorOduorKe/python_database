import db_conn
from db_conn import conn
from dotenv import load_dotenv
import os
import json

load_dotenv()

table_name = os.getenv('table_name')
db_name = os.getenv('db_name')
with open('user_data.json', 'r') as file:
    user_data = json.load(file)
#print(user_data)

def insert_data(conn,user_data):
    try:
        cursor=conn.cursor()
        
        cursor.execute(f'USE {db_name}')

        if not user_data:
            print("No user data provided.")
            return
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        row = cursor.fetchone()[0]
        if row > 0:
            print(f"Data already exists in '{table_name}'.")
            return
        
        for user in user_data:
            cursor.execute(
                f"""
                INSERT INTO {table_name} (name,email,password)
                VALUES(%s,%s,%s)
                """,
                (user['name'], user['email'], user['password']))
            conn.commit()
        print(f"Data inserted successfully into '{table_name}'")    
    except Exception as e:
        print(f"Error inserting data: {e}")
    finally:
        cursor.close()
insert_data(conn, user_data)