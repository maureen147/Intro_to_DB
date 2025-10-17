
#!/usr/bin/python3
"""
A Python script that connects to MySQL server
and creates the database 'alx_book_store' if it doesn't exist.
"""

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root'  # change this if your root password is different
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close cursor and connection safely
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
