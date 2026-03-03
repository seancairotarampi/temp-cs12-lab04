# pyright: strict

from typing import Protocol
from common_types import Player

class WinCondition(Protocol):
    def get_winner(self, grid: list[list[str]]) -> Player | None:
        ...

class TokenPhysics(Protocol):
    def apply(self, grid: list[list[str]], row: int, col: int) -> None:
        ...