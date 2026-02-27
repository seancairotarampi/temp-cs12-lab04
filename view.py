# pyright: strict
from model import ConnectTacToeModel
from typing import List
from common_types import Player

class ConnectTacToeView:
    def display_view(self, grid: List[List[str]]) -> None:
        row: List[str]
        for row in grid:
            print(row)
        print("\n")

    def ask_for_coords(self, current_player: Player) -> tuple[int, int]:
        r: int = 0
        c: int = 0
        cp_symbol: str = "A" if current_player == Player.P1 else "B"
        while not 1 <= r <= 6:
            try:
                r = int(input(f"Enter the row where you will put {cp_symbol} [1-6]: "))
            except TypeError:
                print("safety exit. ")
                exit()
            except ValueError:
                print("Invalid input. ")
            
        while not 1 <= c <= 7:
            try:
                c = int(input(f"Enter the column where you will put {cp_symbol} [1-7]: "))
            except ValueError or TypeError:
                print("Invalid input. ")
        return (r - 1, c - 1)

class ConnectTacToeController:
    def __init__(self, model: ConnectTacToeModel, view: ConnectTacToeView) -> None:
        self._model = model
        self._view = view
    
    def run(self) -> None:
        model = self._model
        view = self._view

        while not model.is_game_done:
            r: int
            c: int
            temp: tuple[int, int]
            confirm: bool = False
            view.display_view(model.grid)
            print(f"Current player: {model.current_player}")
            while not confirm:
                temp = view.ask_for_coords(model.current_player)
                confirm = model.choose_cell(*temp)
                if not confirm:
                    print("\nCell occupied or invalid. Try again.")
                    print("\n")
                else:
                    break
            if model.winner:
                break
            confirm = False
            view.display_view(model.grid)
            print(f"Current player: {model.current_player}")
            while not confirm:
                (r, c) = view.ask_for_coords(model.current_player)
                confirm = model.choose_cell(r, c)
                if not confirm:
                    print("\nCell occupied or invalid. Try again.")
                    print("\n")
                else:
                    break
            if model.winner:
                break

        view.display_view(model.grid)
        if model.p1_wins != model.p2_wins:
            print(f"{'P1' if model.winner == Player.P1 else 'P2'} wins!")
        elif model.p1_wins and model.p2_wins:
            print("Both players win. ")
        else:
            print("No one wins. ")
        print("Game over. ")
            
        

            