"""
Authentication: 
An authentication manager is a class that manages user authentication for an application. 
This manager can be implemented as a singleton to ensure that 
only one instance of the authentication manager is used by the application.
"""

class Authentication:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.logged_in_user = None

auth_manager = Authentication()
auth_manager.logged_in_user = 'Alice'
another_auth_manager = Authentication()
print(another_auth_manager.logged_in_user) # Output: 'Alice'
