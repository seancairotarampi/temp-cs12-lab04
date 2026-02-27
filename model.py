# pyright: strict
from common_types import Player, WinConditionType, TokenPhysicsType

class ConnectTacToeModel:
    def __init__(self, win_condition: WinConditionType, token_physics: TokenPhysicsType) -> None:
        self._current_player = Player.P1
        self._win_condition = win_condition
        self._token_physics = token_physics
        self._grid = [
                    [".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", "."]
                    ]

    def choose_cell(self, row: int, col: int) -> bool:
        if self._grid[row][col] != ".":
            return False
        else:
            if self._current_player == Player.P1:
                self._grid[row][col] = "A"
                self._current_player = Player.P2
                return True
            else:
                self._grid[row][col] = "B"
                self._current_player = Player.P1
                return True

    def get_owner(self, row: int, col: int) -> Player | None:
        if self._grid[row][col] == "A":
            return Player.P1
        elif self._grid[row][col] == "B":
            return Player.P2
        else:
            return None
        

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