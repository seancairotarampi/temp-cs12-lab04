# pyright: strict

from common_types import WinConditionType, TokenPhysicsType
from protocols import WinCondition, TokenPhysics
from model import TicTacToe, NotConnectFour, Floating, StrongGravity, WeakGravity

def create_win_condition(win_condition: WinConditionType) -> WinCondition:
    if win_condition == WinConditionType.TIC_TAC_TOE:
        return TicTacToe()
    
    if win_condition == WinConditionType.NOT_CONNECT_FOUR:
        return NotConnectFour()

def create_token_physics(token_physics: TokenPhysicsType) -> TokenPhysics:
    if token_physics == TokenPhysicsType.FLOATING:
        return Floating()

    if token_physics == TokenPhysicsType.STRONG_GRAVITY:
        return StrongGravity()

    if token_physics == TokenPhysicsType.WEAK_GRAVITY:
        return WeakGravity()