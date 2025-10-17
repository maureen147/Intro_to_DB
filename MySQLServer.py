#!/usr/bin/env python3
"""
Script to create alx_book_store database in MySQL
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        print("🔌 Attempting to connect to MySQL...")
        
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            port=3306
        )
        
        if connection.is_connected():
            print("✅ Successfully connected to MySQL!")
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            
            cursor.close()
            return True
        
    except Error as e:
        print(f"Error: {e}")
        return False
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
        
    finally:
        # Handle closing the database connection
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    create_database()