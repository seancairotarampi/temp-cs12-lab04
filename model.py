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
                for j in range(5):
                    if self._grid[i][j] == "A" and self._grid[i][j+1] == "A" and self._grid[i][j+2] == "A":
                        self._p1_wins = True
                    elif self._grid[i][j] == "B" and self._grid[i][j+1] == "B" and self._grid[i][j+2] == "B":
                        self._p2_wins = True
            
            #column check
            for i in range(4):
                for j in range(7):
                    if self._grid[i][j] == "A" and self._grid[i+1][j] == "A" and self._grid[i+2][j] == "A":
                        self._p1_wins = True
                    elif self._grid[i][j] == "B" and self._grid[i+1][j] == "B" and self._grid[i+2][j] == "B":
                        self._p2_wins = True
        if self._p1_wins == True and self._p2_wins == False:
            return Player.P1
        elif self._p1_wins == False and self._p2_wins == True:
            return Player.P2
        else:
            return None

    @property
    def is_game_done(self) -> bool:
        if self._p1_wins == True or self._p2_wins == True:
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