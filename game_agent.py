"""This file contains all the classes you must complete for this project.
You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.
You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random


class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass

def custom_score(game, player):
    """Method to test the different score heuristics"""
    return chaser_score(game, player)

def chaser_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player. 
    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).
    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)
    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # Check if player is looser.
    # Please notice that 'game.is_loser(player)' function is not used to improve  
    # the performance (game.get_legal_moves(player) is invoked once; otherwise it 
    # would be invoked twice).  ;-)
    player_legal_moves = game.get_legal_moves(player)
    player_moves = len(player_legal_moves)
    if player_moves == 0 and game.active_player == player:
        return float("-inf")

    # Check if player is winner.
    # Please notice that 'game.is_winner(player)' function is not used to improve  
    # the performance (game.get_legal_moves(player) is invoked once; otherwise it 
    # would be invoked twice).  :-)
    opp_player_legal_moves = game.get_legal_moves(game.get_opponent(player))
    opp_player_moves = len(opp_player_legal_moves)
    if opp_player_moves == 0 and game.active_player != player:
        return float("inf")

    # Return the difference of moves between the active player moves and the opponent's
    # having into consideration the spaces where both players overlap.
    players_overlap = [x  for x in player_legal_moves if x in opp_player_legal_moves]
    return float(len(players_overlap)*2 + player_moves - opp_player_moves)

def easy_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player. It calculates the difference of moves between the
    active player moves and the opponent's.
    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).
    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)
    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # Check if player is looser.
    # Please notice that 'game.is_loser(player)' function is not used to improve  
    # the performance (game.get_legal_moves(player) is invoked once; otherwise it 
    # would be invoked twice).  ;-)
    player_moves = len(game.get_legal_moves(player))
    if player_moves == 0 and game.active_player == player:
        return float("-inf")

    # Check if player is winner.
    # Please notice that 'game.is_winner(player)' function is not used to improve  
    # the performance (game.get_legal_moves(player) is invoked once; otherwise it 
    # would be invoked twice).  :-)
    opp_player_moves = len(game.get_legal_moves(game.get_opponent(player)))
    if opp_player_moves == 0 and game.active_player != player:
        return float("inf")

    # Return the difference of moves between the active player moves and the opponent's.
    return float(player_moves - opp_player_moves)


def offensive_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player. It calculates the difference of moves between the
    active player moves and twice the opponent's.
    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).
    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)
    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # Check if player is looser.
    # Please notice that 'game.is_loser(player)' function is not used to improve  
    # the performance (game.get_legal_moves(player) is invoked once; otherwise it 
    # would be invoked twice).  ;-)
    player_moves = len(game.get_legal_moves(player))
    if player_moves == 0 and game.active_player == player:
        return float("-inf")

    # Check if player is winner.
    # Please notice that 'game.is_winner(player)' function is not used to improve  
    # the performance (game.get_legal_moves(player) is invoked once; otherwise it 
    # would be invoked twice).  :-)
    opp_player_moves = len(game.get_legal_moves(game.get_opponent(player)))
    if opp_player_moves == 0 and game.active_player != player:
        return float("inf")

    # Return the difference of moves between the active player moves and twice the opponent's.
    return float(player_moves - 2*opp_player_moves)

class CustomPlayer:
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.
    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)
    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.
    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).
    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().
    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=10.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

    def get_move(self, game, legal_moves, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.
        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.
        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************
        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).
        legal_moves : list<(int, int)>
            A list containing legal moves. Moves are encoded as tuples of pairs
            of ints defining the next (row, col) for the agent to occupy.
        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.
        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Perform any required initializations, including selecting an initial
        # move from the game board (i.e., an opening book), or returning
        # immediately if there are no legal moves
        if not legal_moves:
            return (-1, -1)

        # Get first move in case of time out
        next_move = legal_moves[0]

        try:
            # The search method call (alpha beta or minimax) should happen in
            # here in order to avoid timeout. The try/except block will
            # automatically catch the exception raised by the search method
            # when the timer gets close to expiring

            if self.method == 'minimax':
                search_method = self.minimax
            else: # use alphabeta by default
                search_method = self.alphabeta

            if self.iterative:
                depth = 1
                value = 0
                while value != float("inf") and value != float("-inf"):
                    value, next_move = search_method(game, depth)
                    depth += 1
            else:
                next_move = search_method(game, self.search_depth)[1]

        except Timeout:
            # Do nothing
            pass

        # Return the best move from the last completed search iteration
        return next_move

    def minimax(self, game, depth, maximizing_player=True):
        """Implement the minimax search algorithm as described in the lectures.
        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state
        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting
        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)
        Returns
        -------
        float
            The score for the current search branch
        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves
        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        
        # Check if timeout
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # Check if there are available moves
        available_moves = game.get_legal_moves()
        if not available_moves:
            return (float("-inf"), (-1, -1)) if game.active_player == self else (float("inf"), (-1, -1))

        if depth > 1:
            # Use recursion to navigate until the desired depth
            values = [(self.minimax(game.forecast_move(move), depth - 1, not maximizing_player)[0], move) for move in available_moves]
        else:
            values = [(self.score(game.forecast_move(move), self), move) for move in available_moves]
        
        # Return max value if it is a MAX level or min value otherwise.
        return max(values) if maximizing_player else min(values)


    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        """Implement minimax search with alpha-beta pruning as described in the
        lectures.
        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state
        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting
        alpha : float
            Alpha limits the lower bound of search on minimizing layers
        beta : float
            Beta limits the upper bound of search on maximizing layers
        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)
        Returns
        -------
        float
            The score for the current search branch
        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves
        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """

        # Check if timeout
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # Check if there are available moves
        available_moves = game.get_legal_moves()
        if not available_moves:
            return (float("-inf"), (-1, -1)) if game.active_player == self else (float("inf"), (-1, -1))
        
        values = []
        for move in available_moves:
            if depth > 1:
                # Use recursion to navigate until the desired depth
                value = self.alphabeta(game.forecast_move(move), depth - 1, alpha, beta, not maximizing_player)[0]
            else:
                # Score this level
                value = self.score(game.forecast_move(move), self)

            values.append((value, move))

            if maximizing_player:
                # Check if it is possible to prune
                if value >= beta:
                    break
                # Update alpha when needed
                if value > alpha:
                    alpha = value
            else:
                # Check if it is possible to prune
                if value <= alpha:
                    break
                # Update beta when needed
                if value < beta:
                    beta = value

        return max(values) if maximizing_player else min(values)