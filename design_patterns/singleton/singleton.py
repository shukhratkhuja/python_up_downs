"""
Consider a scenario where you have a database that needs to be shared across different parts of the application. 
You want to ensure that only one instance of the database exists in the entire application. 
You can implement this scenario using the singleton pattern as follows:
"""

class Database:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._data = {}

    def add_data(self, key, value):
        self._data[key] = value

    def get_data(self, key):
        return self._data.get(key)

db1 = Database()
db2 = Database()

print(db1 is db2)

# Output: True
"""
EXAMPLE 1:
In this example, the __new__ method of the Database class is 
overridden to ensure that only one instance of the class is created. 
The first time an instance of the Database class is created, 
the __new__ method creates a new instance and stores it in the _instance attribute. 
Subsequent calls to __new__ simply return the stored instance, 
ensuring that only one instance of the class exists in the entire application.
"""

