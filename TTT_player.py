import math, random


class player:

    def __init__(self, letter):
        ##letter is X or O#
        self.letter = letter

    def get_move(self, game):
        pass


class random_pc_player(player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, TTT_game):
        square = random.choice(TTT_game.available_moves())
        return square


class human_player(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, TTT_game):

        valid_square = False
        value = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                value = int(square)
                if value not in TTT_game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('invalid move enter another one')

        return value


class super_AI(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, TTT_game):
        if len(TTT_game.available_moves()) == 9:
            square = random.choice(TTT_game.available_moves())
        else:
            square = self.minimax(TTT_game, self.letter)['position']

        return square

    def minimax(self, state, player):

        max_player = self.letter
        other_player = "O" if player == "X" else "X"

        if state.current_winner == other_player:

            return { "position" : None,
                     "score"    : 1 * (state.num_empty_squares() + 1) if other_player == max_player else
                                -1 * (state.num_empty_squares() + 1)

                    }

        elif not state.empty_squares():
            return { 'position' : None,
                     'score' : 0
                     }

        if player == max_player:
            best = { 'position': None , 'score' : -math.inf}

        else:
            best = { 'position': None , 'score' : math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)

            sim_score = self.minimax(state, other_player)

            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score

            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best


