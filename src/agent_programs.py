import traceback
import random
import time

from une_ai.assignments import ConnectFourGame
from connect_four_environment import ConnectFourEnvironment
from une_ai.models import GraphNode

# A simple agent program choosing actions randomly
def random_behaviour(percepts, actuators):
    try:
        game_state = {
            'game-board': percepts['game-board-sensor'],
            'power-up-Y': percepts['powerups-sensor']['Y'],
            'power-up-R': percepts['powerups-sensor']['R'],
            'player-turn': percepts['turn-taking-indicator']
        }
    except KeyError as e:
        game_state = {}
        print("You may have forgotten to add the necessary sensors:")
        traceback.print_exc()
    if not ConnectFourEnvironment.is_terminal(game_state):
        legal_moves = ConnectFourEnvironment.get_legal_actions(game_state)
        try:
            action = random.choice(legal_moves)
        except IndexError as e:
            print("You may have forgotten to implement the ConnectFourEnvironment methods, or you implemented them incorrectly:")
            traceback.print_exc()
            return []
        return [action]
    else:
        return []

# An agent program to allow a human player to play Connect Four
# see the assignment's requirements for a list of valid keys
# to interact with the game
def human_agent(percepts, actuators):
    action = ConnectFourGame.wait_for_user_input()
    return [action]

# TODO
# complete the agent program to implement an intelligent behaviour for
# the agent player
def intelligent_behaviour(percepts, actuator):
    # workshop code modification
    player_turn = percepts['turn-taking-indicator']
    try:
        game_state = {
            'game-board': percepts['game-board-sensor'],
            'power-up-Y': percepts['powerups-sensor']['Y'],
            'power-up-R': percepts['powerups-sensor']['R'],
            'player-turn': percepts['turn-taking-indicator']
        }
    except KeyError as e:
        game_state = {}
        print("You may have forgotten to add the necessary sensors:")
        traceback.print_exc()
    max_depth = 4
    if not ConnectFourEnvironment.is_terminal(game_state):
        state_node = GraphNode(game_state, None, None, 0)
        # v1, best_move_1 = minimax(state_node, player_turn, max_depth)
        _, best_move = minimax_alpha_beta(state_node, player_turn, float("-Inf"), float("+Inf"), max_depth)
        if best_move is not None:
            return [best_move] 
    return []

def minimax_alpha_beta(node, player, alpha, beta, depth):
    game_state = node.get_state()
    move_best = None
    player_turn = game_state['player-turn']
    is_maximising = player_turn == player

    legal_actions = ConnectFourEnvironment.get_legal_actions(game_state)

    if is_maximising:
        value = float('-Inf')
    else:
        value = float('+Inf')
    if depth <= 0 or ConnectFourEnvironment.is_terminal(game_state):
        value = ConnectFourEnvironment.payoff(game_state, player)
        return value, move_best
    for action in legal_actions:
        new_state =  ConnectFourEnvironment.transition_result(game_state, action)
        child_node = GraphNode(new_state, node, action, 1)
        value_new, _ = minimax_alpha_beta(child_node, player, alpha, beta, depth - 1)
        if is_maximising:
            if value_new > value:
                value = value_new
                move_best = action
            alpha = max(value, alpha)
            if value >= beta:
                break
        else:
            if value_new < value:
                value = value_new
                move_best = action
            beta = min(value, beta)
            if value <= alpha:
                break
    return value, move_best

def minimax(node, player, depth):
    move_best = None
    game_state = node.get_state()
    player_turn = game_state['player-turn']
    is_maximising = player_turn == player
    
    if is_maximising:
        value = float('-Inf')
    else:
        value = float('+Inf')
    if depth <= 0 or ConnectFourEnvironment.is_terminal(game_state):
        value = ConnectFourEnvironment.payoff(game_state, player)
        return value, move_best
    
    legal_actions = ConnectFourEnvironment.get_legal_actions(game_state)
    for action in legal_actions:
        new_state = ConnectFourEnvironment.transition_result(game_state, action)
        child_node = GraphNode(new_state, node, action, 1)
        value_new, _ = minimax(child_node, player, depth - 1)
        if (is_maximising and value_new > value) or (not is_maximising and value_new < value):
            value = value_new
            move_best = action

    return value, move_best
