
from sample_players import DataPlayer
from functools import reduce
import random

DEPHT_VALUE = 3

class CustomPlayer(DataPlayer):
    """ Implement your own agent to play knight's Isolation
    The get_action() method is the only required method for this project.
    You can modify the interface for get_action by adding named parameters
    with default values, but the function MUST remain compatible with the
    default interface.
    **********************************************************************
    NOTES:
    - The test cases will NOT be run on a machine with GPU access, nor be
      suitable for using any other machine learning techniques.
    - You can pass state forward to your agent on the next turn by assigning
      any pickleable object to the self.context attribute.
    **********************************************************************
    """

    def get_action(self, state):
        """ Employ an adversarial search technique to choose an action
        available in the current state calls self.queue.put(ACTION) at least
        This method must call self.queue.put(ACTION) at least once, and may
        call it as many times as you want; the caller will be responsible
        for cutting off the function after the search time limit has expired.
        See RandomPlayer and GreedyPlayer in sample_players for more examples.
        **********************************************************************
        NOTE:
        - The caller is responsible for cutting off search, so calling
          get_action() from your own code will create an infinite loop!
          Refer to (and use!) the Isolation.play() function to run games.
        **********************************************************************
        """
        
    def __init__(self, player_id):
        super().__init__(player_id)

    def get_action(self, state):
        """ Employ an adversarial search technique to choose an action
        available in the current state calls self.queue.put(ACTION) at least
        This method must call self.queue.put(ACTION) at least once, and may
        call it as many times as you want; the caller will be responsible
        for cutting off the function after the search time limit has expired.
        See RandomPlayer and GreedyPlayer in sample_players for more examples.
        **********************************************************************
        NOTE:
        - The caller is responsible for cutting off search, so calling
          get_action() from your own code will create an infinite loop!
          Refer to (and use!) the Isolation.play() function to run games.
        **********************************************************************
        """

        """ Retrieve transposition table """
        if state.ply_count < 2:
            self.queue.put(random.choice(state.actions()))
        else:
            self.queue.put(self.alpha_beta_search(state, depth=DEPHT_VALUE))

    def alpha_beta_search(self, state, depth):
        """
            The function implements alpha beta search 

            Parameters:
                self (obj): 
                    self class instance reference
                state (obj): 
                    state object
                depth (obj): 
                    Depht of the search

            Returns:
                the next movement position
        """   

        
        
        def minimun_value(state, alpha, beta, depth):
            """
                The function gets the minimun value of all nodes in the search tree

                Parameters:
                    self (obj): 
                        self class instance reference
                    state (obj): 
                        state object
                    alpha (obj): 
                        alpha delta
                    beta (obj): 
                        beta delta
                    depth (obj): 
                        Depht of the search

                Returns:
                    The minimun cost
            """  
            if state.terminal_test():
                return state.utility(self.player_id)

            if depth <= 0: 
                return self.utility_score(state)

            min_val = float("inf")

            for action in state.actions():
                min_val = min(min_val, maximun_value(state.result(action), alpha, beta, depth - 1))

                if min_val <= alpha:
                    return min_val
                beta = min(beta, min_val)

            return min_val           

        
       

#         def max_value(state, alpha, beta, depth):
#             if state.terminal_test(): return state.utility(self.player_id)
#             if depth <= 0: return self.score(state)
#             value = float("-inf")
#             for action in state.actions():
#                 value = max(value, min_value(state.result(action), alpha, beta, depth-1))
#                 if value >= beta:
#                     alpha = max(alpha, value)
#             return value
        
        
        def maximun_value(state, alpha, beta, depth):
            """
                The function gets the maximun cost

                Parameters:
                    self (obj): 
                        self class instance reference
                    state (obj): 
                        state object
                    alpha (obj): 
                        alpha delta
                    beta (obj): 
                        beta delta
                    depth (obj): 
                        Depht of the search

                Returns:
                    The minimun cost
            """  

            if state.terminal_test():
                return state.utility(self.player_id)

            if depth <= 0: 
                return self.utility_score(state)

            max_val = float("-inf")

            for action in state.actions():
                max_val = max(max_val, minimun_value(state.result(action), alpha, beta, depth - 1))

                if max_val >= beta:
                    alpha = max(alpha, max_val)

            return max_val               
        
        
        def get_best_move(best_options, next_action):
            """
                The function gets the maximun cost

                Parameters:
                    best_options (obj): 
                        list of best options searched
                    next_action (obj): 
                        nexto move array detail

                Returns:
                    The minimun cost
            """              
            (best_move, best_score, alpha) = best_options
            
            # Calculates the min cost for the search
            min_value = minimun_value(state.result(next_action), alpha, float("-inf"), depth-1)
            
            alpha = max(alpha, min_value)
            
            return (next_action, min_value, alpha) if min_value >= best_score else (best_move, best_score, alpha)

            

        return reduce(get_best_move, state.actions(), (None, float("-inf"), float("-inf")))[0]

    def utility_score(self, state):
        """
            The function utility_score obtains the score for the players move

            Parameters:
                self (obj): 
                    self class instance reference
                state (obj): 
                    state object

             Returns:
                scores the player movement
        """          
        
        # Get the players localization
        player_localization = state.locs[self.player_id]
        opponent_localization = state.locs[1 - self.player_id]
        
        # Get the players liberties
        player_liberties = state.liberties(player_localization)
        opponent_liberties = state.liberties(opponent_localization)

        # Check the players liberties availables
        available_player_liberties = sum(len(state.liberties(l)) for l in player_liberties)
        available_opponent_liberties = sum(len(state.liberties(l)) for l in opponent_liberties)
        return len(player_liberties) - 2 * len(opponent_liberties) + available_player_liberties - 2 * available_opponent_liberties 