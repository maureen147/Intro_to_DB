#!/usr/bin/env python3
"""
Script to create alx_book_store database in MySQL
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            port=3306
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            cursor.close()
            return True
        
    except Error as e:
        print(f"Error: {e}")
        return False
    finally:
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()