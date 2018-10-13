class CheckersGame:
    dimension_of_board = 8
    row_names = [str(i) for i in range(1, dimension_of_board + 1)]
    column_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    
    
    def __init__(self):
        self.initialize_board()
        self.update_jump_availability()
        self.current_player = 0
        
    
    def initialize_board(self):
        self.board = [[None for j in range(CheckersGame.dimension_of_board)] for i in range(CheckersGame.dimension_of_board)]
        for i in range(CheckersGame.dimension_of_board):
            if i % 2 == 1:
                self.board[0][i] = 1
                self.board[CheckersGame.dimension_of_board - 2][i] = 0
            else:
                self.board[1][i] = 1
                self.board[CheckersGame.dimension_of_board - 1][i] = 0
                
                
    def get_piece(self, position):
        return self.board[position[0]][position[1]]
    
    
    def set_piece(self, position, value):
        self.board[position[0]][position[1]] = value


    def update_turn(self):
        self.current_player = 1 - self.current_player
                
    
    def update_jump_availability(self):
        '''
        This function updates the self.is_jump_available variable, which is a list of booleans for whether or not 
        '''
        is_jump_available = [False, False]
        
        for i in range(CheckersGame.dimension_of_board):
            for j in range(CheckersGame.dimension_of_board):
                for player in (0, 1):
                    if self.board[i][j] == player and self.is_jump_available_at_position_for_player((i, j), player):
                        is_jump_available[player] = True
                        # print(f'Jump available at position {i},{j} for player {player}')
        
        self.is_jump_available = is_jump_available
                    
                
    def is_jump_available_at_position_for_player(self, position, player):
        i, j = position
        
        # I intentionally used 'if player == 1' instead of 'if player' for clearer code
        if player == 1:
            return (i < CheckersGame.dimension_of_board - 2 and j < CheckersGame.dimension_of_board - 2 and self.board[i + 1][j + 1] == 0 and self.board[i + 2][j + 2] == None) \
                or (i < CheckersGame.dimension_of_board - 2 and j >= 2 and self.board[i + 1][j - 1] == 0 and self.board[i + 2][j - 2] == None)
        elif player == 0:
            return (i >= 2 and j < CheckersGame.dimension_of_board - 2 and self.board[i - 1][j + 1] == 1 and self.board[i - 2][j + 2] == None) \
                or (i >= 2 and j >= 2 and self.board[i - 1][j - 1] == 1 and self.board[i - 2][j - 2] == None)
        
    
    def is_valid_position(self, position):
        return type(position) == str and len(position) == 2 and position[0] in CheckersGame.column_names and position[1] in CheckersGame.row_names
    
    
    def convert_position_to_indices(self, position):
        assert self.is_valid_position(position), 'The position you entered is not valid'
        column, row = position
        return CheckersGame.row_names.index(row), CheckersGame.column_names.index(column)
        
    
    def is_valid_jump(self, player, source, destination):
        # (2 * player - 1) equals 1 for player 1 and -1 for player 0
        # This allows us to take into account the fact that each player must move towards the opponent's side
        row_displacement = (2 * player - 1)
        return (destination[1] == source[1] + 2 \
                and destination[0] == source[0] + 2 * row_displacement \
                and self.board[source[0] + row_displacement][source[1] + 1] == 1 - player) \
            or (destination[1] == source[1] - 2 \
                and destination[0] == source[0] + 2 * row_displacement \
                and self.board[source[0] + row_displacement][source[1] - 1] == 1 - player)
    
    
    def action_type(self, action, player):
        source, destination = action
        # (2 * player - 1) equals 1 for player 1 and -1 for player 0
        if destination[0] == source[0] + (2 * player - 1):
            return 'move'
        elif destination[0] == source[0] + 2 * (2 * player - 1):
            return 'jump'
        
    
    def validate_actions(self, player, actions):
        assert type(actions) == list and len(actions) >= 1, "Your actions are in the wrong format"
        
        current_piece_position = actions[0][0]
        assert self.get_piece(current_piece_position) == player, "The current player does not have a piece in the specified position"
        
        first_action_type = self.action_type(actions[0], player)
        
        assert not (self.is_jump_available[player] and first_action_type == 'move'), 'You are moving, but a jump is available'
            
        assert not (first_action_type == 'move' and len(actions) > 1)
        
        if first_action_type == 'jump':
            for action in actions:
                source, destination = action
                if not (source == current_piece_position and self.is_valid_jump(player, source, destination)):
                    assert False, 'One of your jumps is not valid'
                else:
                    current_piece_position = destination
            
        return not self.is_jump_available_at_position_for_player(current_piece_position, player)
    
    
    def convert_actions_to_indices(self, actions):
        return [(self.convert_position_to_indices(action[0]), self.convert_position_to_indices(action[1])) for action in actions]
    
    
    def position_to_delete(self, source, destination):
        return (int((source[0] + destination[0]) / 2), int((source[1] + destination[1]) / 2))

    
    def take_actions(self, player, actions):
        actions = self.convert_actions_to_indices(actions)
        self.validate_actions(player, actions)
        
        if self.action_type(actions[0], player) == 'move':
            source, destination = actions[0]
            self.set_piece(source, None)
            self.set_piece(destination, player)
            
        if self.action_type(actions[0], player) == 'jump':
            self.set_piece(actions[0][0], None)
            for action in actions:
                source, destination = action
                self.set_piece(self.position_to_delete(source, destination), None)
            self.set_piece(actions[-1][1], player)


    def take_turn(self, actions):
        '''
        Takes in a list of actions, and executes the current player's turn
        '''
        self.take_actions(self.current_player, actions)
        self.update_turn()
        self.update_jump_availability()
            
    
    def print_board(self):
        # Some parts of the below printing code is borrowed from https://stackoverflow.com/questions/13214809/pretty-print-2d-python-list
        # I have not changed the variable names from the stackoverflow answer, which is why they are not as descriptive
        s =  [[''] + CheckersGame.column_names] + [[str(row_index + 1)] + [str(e) if e is not None else '-' for e in self.board[row_index]] for row_index in range(len(self.board))]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n')
        print('\n'.join(table))

