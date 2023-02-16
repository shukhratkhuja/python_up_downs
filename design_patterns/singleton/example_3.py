"""
Logger: 
A logger is a class that logs messages from an application. 
This logger can be implemented as a singleton to ensure that 
only one instance of the logger is used by the application.
"""

import logging

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.logger = logging.getLogger('my_logger')
        self.logger.setLevel(logging.DEBUG)

logger = Logger()
logger.logger.info('Logging a message')
another_logger = Logger()
print(another_logger.logger == logger.logger) # Output: True
