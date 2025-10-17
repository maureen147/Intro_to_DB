#!/usr/bin/env python3
"""
Script to create alxbookstore database in MySQL
"""

import mysql.connector
from mysql.connector import Error

# Establish connection to MySQL server
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
    
    # Create database if it doesn't exist
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
    print("Database 'alxbookstore' created successfully!")
    cursor.close()
    connection.close()

except mysql.connector.Error as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"Error: {e}")