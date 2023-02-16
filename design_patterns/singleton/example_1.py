"""
Configuration Manager: 
A configuration manager is a class that provides access to a configuration file or database, 
which is usually read-only. 
This manager can be implemented as a singleton to ensure that 
only one instance of the configuration is loaded and used by the application.
"""

class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.config = {'db_host': 'localhost', 'db_port': 5432, 'db_name': 'my_db'}

config_manager = ConfigurationManager()
config_manager.config['db_host'] = '192.168.1.1'
another_config_manager = ConfigurationManager()
print(another_config_manager.config['db_host']) # Output: '192.168.1.1'
