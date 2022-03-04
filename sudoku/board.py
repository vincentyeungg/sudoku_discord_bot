from random import shuffle

class Board:
    """
    This class represents a 9x9 Sudoku game board.
    """
    
    def __init__(self) -> None:
        # initial board is 9x9 board with empty values depicted by 0's
        self.board = self.generate_empty_sudoku_board()
        
        
    def generate_empty_sudoku_board(self):
        return [[0 for i in range(9)] for j in range(9)]
    
    
    def generate_starting_sudoku_board(self, difficulty):
        # a valid starting sudoku board must have 17 clues
        # for difficulties, adjust the range of the clues given to user
        if difficulty not in range(1,4):
            raise ValueError(f"Invalid difficulty. Difficulty must be level 1, 2 or 3.")
        
        num_of_clues = self._number_of_clues_based_on_difficulty(difficulty)
        
        # to generate starting sudoku board, first find a solution and then remove random elements from the board
        # to ensure a valid solution each time
        valid_nums = [x for x in range(1,10)]
        for i in range(81):
            # iterate from 0-8
            row = i // 9
            col = i % 9
            
            # determine if cell is empty (denoted by 0)
            if self.board[row][col] == 0:
                shuffle(valid_nums)
                
                # if empty value, find a num from 1-9, and determine if the location is suitable for this number
                # without breaking sudoku constraints
                for num in valid_nums:
                    # implement
                    pass
        
            
    def _number_of_clues_based_on_difficulty(self, difficulty):
        # easy difficulty
        if difficulty == 1:
            num_clues = (25, 28)
            
        # medium
        elif difficulty == 2:
            num_clues = (21, 24)
            
        # hard
        elif difficulty == 3:
            num_clues = (17, 21)
            
        # shuffle values from specified range, and return the first element of the random sequence 
        random_num = [num for num in range(num_clues[0], num_clues[-1] + 1)]
        shuffle(random_num)
        return random_num[0]
    
    def _valid_location(self, num, row, col):
        # implement
        pass