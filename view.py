# pyright: strict
from model import ConnectTacToeModel
from typing import List
from common_types import Player

class ConnectTacToeView:
    def display_view(self, current_player: Player, grid: List[List[str]], ) -> None:
        row: List[str]
        for row in grid:
            print(row)
        print("\n")
        
        print(f"Current player: {current_player}")

    def ask_for_coords(self, current_player: Player) -> tuple[int, int]:
        r: int = -1
        c: int = -1
        cp_symbol: str = "A" if current_player == Player.P1 else "B"
        while 1 <= r <= 7:
            try:
                r = int(input(f"Enter the row where you will put {cp_symbol} [1-7]: "))
            except ValueError or TypeError:
                continue
        while 1 <= c <= 8:
            try:
                c = int(input(f"Enter the column where you will put {cp_symbol} [1-8]: "))
            except ValueError or TypeError:
                continue
        return (r, c)

class ConnectTacToeController:
    def __init__(self, model: ConnectTacToeModel, view: ConnectTacToeView) -> None:
        self._model = model
        self._view = view
    
    def run(self) -> None:
        model = self._model
        view = self._view

        while not model.is_game_done:
            r: int = -1
            c: int = -1
            confirm: bool = False
            view.display_view(model.current_player, model.grid)
            while not confirm:
                (r, c) = view.ask_for_coords(model.current_player)
                confirm = model.choose_cell(r, c)
                if confirm == False:
                    print("\nCell occupied or invalid. Try again.")
                    print("\n")
            
        

            