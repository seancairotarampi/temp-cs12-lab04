from argparse import ArgumentParser
from model import ConnectTacToeModel
from view import ConnectTacToeView, ConnectTacToeController
from common_types import WinConditionType, TokenPhysicsType

parser: ArgumentParser = ArgumentParser()
parser.add_argument("-p", "--token_physics", default="floating")
parser.add_argument("-w", "--win_condition", default="tictactoe")
args = parser.parse_args()

def main() -> None:
    tp: TokenPhysicsType
    wc: WinConditionType
    if args.token_physics == "weak":
        tp = TokenPhysicsType.WEAK_GRAVITY
    elif args.token_physics == "strong":
        tp = TokenPhysicsType.STRONG_GRAVITY
    else:
        tp = TokenPhysicsType.FLOATING
    if args.win_condition == "notconnectfour":
        wc = WinConditionType.NOT_CONNECT_FOUR
    else:
        wc = WinConditionType.TIC_TAC_TOE

    m: ConnectTacToeModel = ConnectTacToeModel(wc, tp)
    v: ConnectTacToeView = ConnectTacToeView()
    c: ConnectTacToeController = ConnectTacToeController(m, v)
    c.run()

if __name__ == "__main__":
    main()