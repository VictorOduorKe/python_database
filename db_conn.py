# import the dependancies

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

host_name = os.getenv('db_host')
user_name = os.getenv('db_user')
user_password = os.getenv('db_password')
db_name = os.getenv('db_name')

def create_connection(host_name,user_name,user_password,db_name):
    try:    
        connection=mysql.connector.connect(
        host=host_name,
        user=user_name,
        password=user_password
    )
        print("Connection to MySQL DB successful")
        cursor=connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"Database {db_name} created successfully")
        cursor.execute(f"USE {db_name}")
        cursor.close()
    except Error as e:
        print(f"Error: {e}")
    return connection
conn=create_connection(host_name,user_name,user_password,db_name)
