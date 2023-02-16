"""
Command Pattern:
The Command Pattern allows you to encapsulate requests as objects, 
so you can queue or log them and support undo-redo operations. 
This is useful when you want to decouple the requester of a command 
from the object that performs it.


Example: 
Suppose you have a remote control that can control 
multiple devices (TV, DVD player, etc.). 
You can implement a Command Pattern to encapsulate 
each device's actions as a command object. 
Here's some sample code in Python:

"""


class Command:
    def execute(self):
        pass

class TvOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_on()

class RemoteControl:
    def __init__(self, commands):
        self.commands = commands

    def press_button(self, button):
        self.commands[button].execute()
