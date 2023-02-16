"""
Command Manager: 
A command manager is a class that manages the execution of commands in an application. 
This manager can be implemented as a singleton to ensure that 
only one instance of the command manager is used by the application.
"""

class CommandManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

command_manager = CommandManager()
command_manager.add_command('open_file')
another_command_manager = CommandManager()
print(another_command_manager.commands) # Output: ['open_file']
