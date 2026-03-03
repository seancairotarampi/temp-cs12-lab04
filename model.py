# pyright: strict

from common_types import Player, WinConditionType, TokenPhysicsType

class ConnectTacToeModel:
    def __init__(self, win_condition: WinConditionType, token_physics: TokenPhysicsType) -> None:
        self._current_player = Player.P1
        self._win_condition = win_condition
        self._token_physics = token_physics
        self._p1_wins = False
        self._p2_wins = False
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
        if self._win_condition == WinConditionType.TIC_TAC_TOE:
            # row check
            for i in range(6):
                if self._grid[i] == ["A", "A", "A", "A", "A", "A", "A"]:
                    self._p1_wins = True
                elif self._grid[i] == ["B", "B", "B", "B", "B", "B", "B"]:
                    self._p2_wins = True
            
            #column check
            rotated_grid = [list(row) for row in zip(*self._grid[::-1])]

            for i in range(7):
                if rotated_grid[i] == ["A", "A", "A", "A", "A", "A"]:
                    self._p1_wins = True
                elif rotated_grid[i] == ["B", "B", "B", "B", "B", "B"]:
                    self._p2_wins = True

        if self._p1_wins == True and self._p2_wins == False:
            return Player.P1
        elif self._p1_wins == False and self._p2_wins == True:
            return Player.P2
        else:
            return None

    @property
    def is_game_done(self) -> bool:
        if self._p1_wins or self._p2_wins:
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
        return self._p1_wins
    
    @property
    def p2_wins(self) -> bool:
        return self._p2_wins
    
    def choose_cell(self, row: int, col: int) -> bool:
        if self._grid[row][col] != ".":
            return False
        else:
            if self._current_player == Player.P1:
                self._grid[row][col] = "A"
                self._current_player = Player.P2
            else:
                self._grid[row][col] = "B"
                self._current_player = Player.P1
            
            if self._token_physics == TokenPhysicsType.STRONG_GRAVITY:
                for i in reversed(range(6)):
                    if self._grid[i][col] == ".":
                        self._grid[i][col] = self._grid[row][col]
                        self._grid[row][col] = "."
                        break
            
            if self._token_physics == TokenPhysicsType.WEAK_GRAVITY:
                for i in reversed(range(5)):
                    for j in range(7):
                        if self._grid[i][j] != "." and self._grid[i+1][j] == ".":
                            self._grid[i+1][j] = self._grid[i][j]
                            self._grid[i][j] = "."

            return True
    
    def get_owner(self, row: int, col: int) -> Player | None:
        if self._grid[row][col] == "A":
            return Player.P1
        elif self._grid[row][col] == "B":
            return Player.P2
        else:
            return None

class TicTacToe:
    def get_winner(self, grid: list[list[str]]) -> Player | None:
        p1_wins: bool = False
        p2_wins: bool = False
        # row check
        for i in range(6):
            if grid[i] == ["A", "A", "A", "A", "A", "A", "A"]:
                p1_wins = True
            elif grid[i] == ["B", "B", "B", "B", "B", "B", "B"]:
                p2_wins = True
            
        #column check
        rotated_grid = [list(row) for row in zip(*grid[::-1])]

        for i in range(7):
            if rotated_grid[i] == ["A", "A", "A", "A", "A", "A"]:
                p1_wins = True
            elif rotated_grid[i] == ["B", "B", "B", "B", "B", "B"]:
                p2_wins = True
        
        if p1_wins == True and p2_wins == False:
            return Player.P1
        elif p1_wins == False and p2_wins == True:
            return Player.P2
        else:
            return None

class NotConnectFour:
    def get_winner(self, grid: list[list[str]]) -> Player | None:
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