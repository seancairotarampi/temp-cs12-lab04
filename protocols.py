# pyright: strict

from typing import Protocol

class WinCondition(Protocol):    
    @property
    def p1_wins(self) -> bool: # returns whether or not player 1 wins
        ...
    
    @property
    def p2_wins(self) -> bool: # returns whether or not player 2 wins
        ...

    def update_player_state(self, grid: list[list[str]]) -> None: # Updates the state of the player (if theyre winning or not)
        ...

class TokenPhysics(Protocol):
    def apply(self, grid: list[list[str]], row: int, col: int) -> None: # updates the board based on the token physics
        ...