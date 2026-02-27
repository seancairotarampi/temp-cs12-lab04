# pyright: strict
from common_types import Player, WinConditionType, TokenPhysicsType

class ConnectTacToeModel:
    def __init__(self, p1: Player, p2: Player, win_condition: WinConditionType, token_physics: TokenPhysicsType) -> None:
        ...

    def choose_cell(self, row: int, col: int) -> bool:
        ...

    def get_owner(self, row: int, col: int) -> Player | None:
        ...

    @property
    def current_player(self) -> Player:
        ...

    @property
    def winner(self) -> Player | None:
        ...

    @property
    def is_game_done(self) -> bool:
        ...

    @property
    def row_count(self) -> int:
        ...

    @property
    def col_count(self) -> int:
        ...