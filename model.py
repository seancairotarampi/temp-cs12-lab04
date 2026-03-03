# pyright: strict

from common_types import Player, WinConditionType, TokenPhysicsType
from protocols import WinCondition, TokenPhysics

class ConnectTacToeModel:
    def __init__(self, win_condition: WinConditionType, token_physics: TokenPhysicsType) -> None:
        self._current_player = Player.P1
        self._win_condition = create_win_condition(win_condition)
        self._token_physics = create_token_physics(token_physics)
        self._grid = [
                    [".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", "."]
                    ]

    @property
    def current_player(self) -> Player:
        return self._current_player

    @property
    def winner(self) -> Player | None:
        self._win_condition.update_player_state(self._grid)

        if self._win_condition.p1_wins == True and self._win_condition.p2_wins == False:
            return Player.P1
        elif self._win_condition.p1_wins == False and self._win_condition.p2_wins == True:
            return Player.P2
        else:
            return None

    @property
    def is_game_done(self) -> bool:
        self._win_condition.update_player_state(self._grid)

        if self._win_condition.p1_wins or self._win_condition.p2_wins: # someone wins
            return True
        
        # check for empty cells
        for i in range(6):
            for j in range(7):
                if self._grid[i][j] == ".":
                    return False
        
        return True

    @property
    def row_count(self) -> int:
        return 6

    @property
    def col_count(self) -> int:
        return 7
    
    @property
    def grid(self) -> list[list[str]]:
        return self._grid
    
    @property
    def p1_wins(self) -> bool:
        self._win_condition.update_player_state(self._grid)
        return self._win_condition.p1_wins
    
    @property
    def p2_wins(self) -> bool:
        self._win_condition.update_player_state(self._grid)
        return self._win_condition.p2_wins
    
    def choose_cell(self, row: int, col: int) -> bool:
        if self._grid[row][col] != ".":
            return False
        token = "A" if self._current_player == Player.P1 else "B"
        self._grid[row][col] = token    
        self._token_physics.apply(self._grid, row, col)
        self._current_player = (Player.P2 if self._current_player == Player.P1 else Player.P1)
        return True
    
    def get_owner(self, row: int, col: int) -> Player | None:
        if self._grid[row][col] == "A":
            return Player.P1
        elif self._grid[row][col] == "B":
            return Player.P2
        else:
            return None

class TicTacToe:
    def __init__(self):
        self._p1_wins: bool = False
        self._p2_wins: bool = False
    
    @property
    def p1_wins(self) -> bool:
        return self._p1_wins
    
    @property
    def p2_wins(self) -> bool:
        return self._p2_wins
    
    def update_player_state(self, grid: list[list[str]]) -> None:
        # row check
        for i in range(6):
            if grid[i] == ["A", "A", "A", "A", "A", "A", "A"]:
                self._p1_wins = True
            if grid[i] == ["B", "B", "B", "B", "B", "B", "B"]:
                self._p2_wins = True
            
        #column check
        rotated_grid = [list(row) for row in zip(*grid[::-1])]

        for i in range(7):
            if rotated_grid[i] == ["A", "A", "A", "A", "A", "A"]:
                self._p1_wins = True
            if rotated_grid[i] == ["B", "B", "B", "B", "B", "B"]:
                self._p2_wins = True

class NotConnectFour:
    @property
    def p1_wins(self) -> bool:
        ...
    
    @property
    def p2_wins(self) -> bool:
        ...

    def update_player_state(self, grid: list[list[str]]) -> None:
        ...

class Floating:
    def apply(self, grid: list[list[str]], row: int, col: int) -> None:
        pass

class StrongGravity:
    def apply(self, grid: list[list[str]], row: int, col: int) -> None:
        for i in reversed(range(6)):
            if grid[i][col] == ".":
                grid[i][col] = grid[row][col]
                grid[row][col] = "."
                break

class WeakGravity:
    def apply(self, grid: list[list[str]], row: int, col: int) -> None:
        for i in reversed(range(5)):
            for j in range(7):
                if grid[i][j] != "." and grid[i+1][j] == ".":
                    grid[i+1][j] = grid[i][j]
                    grid[i][j] = "."

#sets win condition
def create_win_condition(win_condition: WinConditionType) -> WinCondition:
    if win_condition == WinConditionType.TIC_TAC_TOE:
        return TicTacToe()
    
    if win_condition == WinConditionType.NOT_CONNECT_FOUR:
        return NotConnectFour()

#sets token physics
def create_token_physics(token_physics: TokenPhysicsType) -> TokenPhysics:
    if token_physics == TokenPhysicsType.FLOATING:
        return Floating()

    if token_physics == TokenPhysicsType.STRONG_GRAVITY:
        return StrongGravity()

    if token_physics == TokenPhysicsType.WEAK_GRAVITY:
        return WeakGravity()