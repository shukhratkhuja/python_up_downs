"""
User Preferences: 
A user preferences manager is a class that manages user preferences for an application. 
This manager can be implemented as a singleton to ensure that 
only one instance of the user preferences is used by the application.
"""

class UserPreferences:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.preferences = {'theme': 'dark', 'language': 'en'}

user_preferences = UserPreferences()
user_preferences.preferences['theme'] = 'light'
another_user_preferences = UserPreferences()
print(another_user_preferences.preferences['theme']) # Output: 'light'
