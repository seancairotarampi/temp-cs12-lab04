# pyright: strict

from common_types import Player, WinConditionType, TokenPhysicsType
from model import ConnectTacToeModel

def test_properties():
    # default conditions
    win_condition = WinConditionType.TIC_TAC_TOE
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.grid == [
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."]
                        ]
    assert model.current_player == Player.P1
    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == False
    assert model.p2_wins == False
    assert model.winner == None
    assert not model.is_game_done

def test_choose_cell():
    win_condition = WinConditionType.TIC_TAC_TOE
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.current_player == Player.P1
    assert model.choose_cell(0, 0)
    assert model.grid == [
                        ["A", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."]
                        ]

    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == False
    assert model.p2_wins == False
    assert model.winner == None
    assert not model.is_game_done

def test_choose_cell_choose_occupied_cell():
    win_condition = WinConditionType.TIC_TAC_TOE
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.current_player == Player.P1
    assert model.choose_cell(0, 0) 
    assert model.current_player == Player.P2
    assert not model.choose_cell(0, 0) # choice rejected
    assert model.grid == [
                        ["A", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."]
                        ]
    assert model.current_player == Player.P2 # still player two's turn

    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == False
    assert model.p2_wins == False
    assert model.winner == None
    assert not model.is_game_done

def test_choose_cell_player_two():
    win_condition = WinConditionType.TIC_TAC_TOE
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.current_player == Player.P1
    assert model.choose_cell(0, 0)
    assert model.current_player == Player.P2
    assert model.choose_cell(0, 1)
    assert model.grid == [
                        ["A", "B", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."]
                        ]

    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == False
    assert model.p2_wins == False
    assert model.winner == None
    assert not model.is_game_done

def test_get_owner():
    win_condition = WinConditionType.TIC_TAC_TOE
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.current_player == Player.P1
    assert model.choose_cell(0, 0)
    assert model.current_player == Player.P2
    assert model.choose_cell(0, 1)
    assert model.grid == [
                        ["A", "B", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."]
                        ]
    assert model.get_owner(0, 0) == Player.P1
    assert model.get_owner(0, 1) == Player.P2
    assert model.get_owner(0, 2) == None

    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == False
    assert model.p2_wins == False
    assert model.winner == None
    assert not model.is_game_done

def test_fill_board():
    win_condition = WinConditionType.TIC_TAC_TOE
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    for i in range(6):
        for j in range(7):
            assert model.choose_cell(i, j)
    
    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == False
    assert model.p2_wins == False
    assert model.winner == None
    assert model.is_game_done

def test_both_players_win():
    win_condition = WinConditionType.TIC_TAC_TOE
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.choose_cell(0, 0)
    assert model.choose_cell(1, 0)
    assert model.choose_cell(0, 1)
    assert model.choose_cell(1, 1)
    assert model.choose_cell(0, 2)
    assert model.choose_cell(1, 2)
    assert model.choose_cell(0, 3)
    assert model.choose_cell(1, 3)
    assert model.choose_cell(0, 4)
    assert model.choose_cell(1, 4)
    assert model.choose_cell(0, 5)
    assert model.choose_cell(1, 5)
    assert model.choose_cell(0, 6)
    assert model.choose_cell(1, 6)

    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == True
    assert model.p2_wins == True
    assert model.winner == None
    assert model.is_game_done

def test_TicTacToe_Player1_wins_row():
    win_condition = WinConditionType.TIC_TAC_TOE
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.choose_cell(0, 0)
    assert model.choose_cell(1, 0)
    assert model.choose_cell(0, 1)
    assert model.choose_cell(1, 1)
    assert model.choose_cell(0, 2)
    assert model.choose_cell(1, 2)
    assert model.choose_cell(0, 3)
    assert model.choose_cell(1, 3)
    assert model.choose_cell(0, 4)
    assert model.choose_cell(1, 4)
    assert model.choose_cell(0, 5)
    assert model.choose_cell(1, 5)
    assert model.choose_cell(0, 6)

    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == True
    assert model.p2_wins == False
    assert model.winner == Player.P1
    assert model.is_game_done

def test_TicTacToe_Player2_wins_row():
    win_condition = WinConditionType.TIC_TAC_TOE
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.choose_cell(0, 0)
    assert model.choose_cell(1, 0)
    assert model.choose_cell(0, 1)
    assert model.choose_cell(1, 1)
    assert model.choose_cell(0, 2)
    assert model.choose_cell(1, 2)
    assert model.choose_cell(0, 3)
    assert model.choose_cell(1, 3)
    assert model.choose_cell(0, 4)
    assert model.choose_cell(1, 4)
    assert model.choose_cell(0, 5)
    assert model.choose_cell(1, 5)
    assert model.choose_cell(5, 6)
    assert model.choose_cell(1, 6)

    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == False
    assert model.p2_wins == True
    assert model.winner == Player.P2
    assert model.is_game_done

def test_TicTacToe_Player1_wins_col():
    win_condition = WinConditionType.TIC_TAC_TOE
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.choose_cell(0, 0)
    assert model.choose_cell(0, 1)
    assert model.choose_cell(1, 0)
    assert model.choose_cell(1, 1)
    assert model.choose_cell(2, 0)
    assert model.choose_cell(2, 1)
    assert model.choose_cell(3, 0)
    assert model.choose_cell(3, 1)
    assert model.choose_cell(4, 0)
    assert model.choose_cell(4, 1)
    assert model.choose_cell(5, 0)

    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == True
    assert model.p2_wins == False
    assert model.winner == Player.P1
    assert model.is_game_done

def test_TicTacToe_Player2_wins_col():
    win_condition = WinConditionType.TIC_TAC_TOE
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.choose_cell(0, 0)
    assert model.choose_cell(0, 1)
    assert model.choose_cell(1, 0)
    assert model.choose_cell(1, 1)
    assert model.choose_cell(2, 0)
    assert model.choose_cell(2, 1)
    assert model.choose_cell(3, 0)
    assert model.choose_cell(3, 1)
    assert model.choose_cell(4, 0)
    assert model.choose_cell(4, 1)
    assert model.choose_cell(5, 2)
    assert model.choose_cell(5, 1)

    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == False
    assert model.p2_wins == True
    assert model.winner == Player.P2
    assert model.is_game_done

def test_NotConnectFour_empty_grid():
    win_condition = WinConditionType.NOT_CONNECT_FOUR
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)    

    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == False
    assert model.p2_wins == False
    assert model.winner == None
    assert not model.is_game_done

def test_NotConnectFour_not_group():
    win_condition = WinConditionType.NOT_CONNECT_FOUR
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.choose_cell(0, 0)
    assert model.choose_cell(1, 0)
    assert model.choose_cell(0, 1)
    assert model.choose_cell(1, 1)
    assert model.choose_cell(0, 2)

    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == False
    assert model.p2_wins == False
    assert model.winner == None
    assert not model.is_game_done

def test_NotConnectFour_Player1_wins():
    win_condition = WinConditionType.NOT_CONNECT_FOUR
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.choose_cell(0, 0)
    assert model.choose_cell(1, 0)
    assert model.choose_cell(0, 1)
    assert model.choose_cell(1, 1)
    assert model.choose_cell(0, 2)
    assert model.choose_cell(1, 2)
    assert model.choose_cell(0, 3)

    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == True
    assert model.p2_wins == False
    assert model.winner == Player.P1
    assert model.is_game_done

def test_NotConnectFour_Player2_wins():
    win_condition = WinConditionType.NOT_CONNECT_FOUR
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.choose_cell(0, 0)
    assert model.choose_cell(0, 1)
    assert model.choose_cell(1, 0)
    assert model.choose_cell(1, 1)
    assert model.choose_cell(2, 0)
    assert model.choose_cell(2, 1)
    assert model.choose_cell(3, 5)
    assert model.choose_cell(3, 1)

    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == False
    assert model.p2_wins == True
    assert model.winner == Player.P2
    assert model.is_game_done

def test_NotConnectFour_group_of_five():
    win_condition = WinConditionType.NOT_CONNECT_FOUR
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.choose_cell(0, 0)
    assert model.choose_cell(1, 0)
    assert model.choose_cell(0, 1)
    assert model.choose_cell(4, 4)
    assert model.choose_cell(0, 2)
    assert model.choose_cell(1, 2)
    assert model.choose_cell(1, 1)
    assert model.choose_cell(3, 3)
    assert model.choose_cell(0, 3)

    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == True
    assert model.p2_wins == False
    assert model.winner == Player.P1
    assert model.is_game_done

def test_NotConnectFour_both_players_win():
    win_condition = WinConditionType.NOT_CONNECT_FOUR
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.choose_cell(0, 0)
    assert model.choose_cell(0, 1)
    assert model.choose_cell(1, 0)
    assert model.choose_cell(1, 1)
    assert model.choose_cell(2, 0)
    assert model.choose_cell(2, 1)
    assert model.choose_cell(3, 0)
    assert model.choose_cell(3, 1)

    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == True
    assert model.p2_wins == True
    assert model.winner == None
    assert model.is_game_done

def test_Floating():
    win_condition = WinConditionType.TIC_TAC_TOE
    token_physics = TokenPhysicsType.FLOATING

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.current_player == Player.P1
    assert model.choose_cell(0, 0)

    assert model.get_owner(0, 0) == Player.P1
    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == False
    assert model.p2_wins == False
    assert model.winner == None
    assert not model.is_game_done

def test_StrongGravity():
    win_condition = WinConditionType.TIC_TAC_TOE
    token_physics = TokenPhysicsType.STRONG_GRAVITY

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.choose_cell(5, 0)
    assert model.choose_cell(0, 0)

    assert model.get_owner(5, 0) == Player.P1
    assert model.get_owner(4, 0) == Player.P2
    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == False
    assert model.p2_wins == False
    assert model.winner == None
    assert not model.is_game_done

def test_WeakGravity():
    win_condition = WinConditionType.TIC_TAC_TOE
    token_physics = TokenPhysicsType.WEAK_GRAVITY

    model = ConnectTacToeModel(win_condition, token_physics)

    assert model.choose_cell(5, 0)
    assert model.choose_cell(0, 0)

    assert model.get_owner(5, 0) == Player.P1
    assert model.get_owner(1, 0) == Player.P2
    assert model.row_count == 6
    assert model.col_count == 7
    assert model.p1_wins == False
    assert model.p2_wins == False
    assert model.winner == None
    assert not model.is_game_done