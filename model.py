# pyright: strict

class ConnectTacToeModel:
    def __init__(self, win_condition: WinConditionType, token_physics: TokenPhysicsType):
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