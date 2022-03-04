from sudoku.board import Board

import pytest

@pytest.fixture
def sudoku_board():
    empty_board = [
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]
            ]
    return empty_board


def test_create_empty_board(sudoku_board):
    board = Board()
    assert board.board == sudoku_board

    
# def test_initialize_board_with_values():
#     board = Board()
#     # need to figure out how to test random board
#     board.generate_starting_sudoku_board(1)

    
def test_generate_number_of_clues_based_on_difficulty():
    board = Board()
    num_of_clues = board._number_of_clues_based_on_difficulty(1)
    assert num_of_clues in range(25, 29)
    

def test_valid_location_on_board_for_number():
    # implement
    pass