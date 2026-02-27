# pyright: strict
from model import ConnectTacToeModel

class ConnectTacToeView:
    def display_view(self):
        ...

class ConnectTacToeController:
    def __init__(self, model: ConnectTacToeModel, view: ConnectTacToeView) -> None:
        pass
    
    def run(self) -> None:
        ...