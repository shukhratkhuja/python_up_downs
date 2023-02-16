"""
Database Connection: 
A database connection manager is a class that provides access to a database. 
This manager can be implemented as a singleton to ensure that 
only one instance of the database connection is created and used by the application.
"""

import psycopg2

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.conn = psycopg2.connect(host='localhost', port=5432, dbname='my_db')

db_conn = DatabaseConnection()
cur = db_conn.conn.cursor()
cur.execute("SELECT * FROM users")
users = cur.fetchall()
another_db_conn = DatabaseConnection()
print(another_db_conn.conn == db_conn.conn) # Output: True
