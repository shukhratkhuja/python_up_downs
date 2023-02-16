"""
Game State: 
A game state manager is a class that manages the state of a game. 
This manager can be implemented as a singleton to ensure that 
only one instance of the game state is used by the game.
"""

class GameState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.score = 0
        self.level = 1

game_state = GameState()
game_state.score += 10
another_game_state = GameState()
print(another_game_state.score) # Output: 10
