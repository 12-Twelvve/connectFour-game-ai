from une_ai.assignments import ConnectFourBaseEnvironment

class ConnectFourEnvironment(ConnectFourBaseEnvironment):
    def __init__(self):
        super().__init__()
    # TODO
    # static method
    # Note: in a static method you do not have access to self
    def get_legal_actions(game_state):
        # it must return the legal actions for the current game state
        try:
            game_board = game_state["game-board"]
            player_turn = game_state['player-turn']
        except:
            print("error in game_state variable")
        legal_actions = []
        for col_num in range(game_board.get_width()):
            if not ConnectFourBaseEnvironment.is_column_full(game_board, col_num):
                legal_actions.append(f'release-{col_num}')
            if player_turn == game_board.get_item_value(col_num, 5):
                legal_actions.append(f'popup-{col_num}')
        return legal_actions
    # TODO
    # static method
    # Note: in a static method you do not have access to self
    def is_terminal(game_state):
        # it must return True if there is a winner or there are no more legal actions, False otherwise
        return  ConnectFourEnvironment.get_winner(game_state) is not None or len(ConnectFourEnvironment.get_legal_actions(game_state)) == 0


    # TODO
    # static method
    # Note: in a static method you do not have access to self
    def payoff(game_state, player_colour):
        # it must return a payoff for the considered player ('Y' or 'R') in a given game_state
        winner_player = ConnectFourBaseEnvironment.get_winner(game_state)
        if winner_player == player_colour:
            return 1
        elif winner_player is not None and winner_player != player_colour:
            return -1
        else:
            return 0 