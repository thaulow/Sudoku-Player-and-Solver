# Assessment 2 @ Noroff University College
_author_ = "Thomas Thaulow"
copyright = "Thomas Thaulow"
_email_ = "thaulow@thaulow.co"

import random

######################################
#======== 6x6 Sudoku Boards =========#
######################################

board1 = [[0, 6, 0, 0, 0, 0],  # Row 0
          [0, 0, 0, 6, 2, 4],  # Row 1
          [3, 0, 4, 0, 1, 0],  # Row 2
          [0, 0, 0, 2, 0, 0],  # Row 3
          [0, 0, 0, 4, 5, 0],  # Row 4
          [0, 0, 1, 0, 0, 2]]  # Row 5

board2 = [[6, 4, 0, 1, 2, 0],  # Row 0
          [1, 0, 2, 0, 0, 4],  # Row 1
          [5, 0, 4, 2, 3, 6],  # Row 2
          [2, 0, 0, 0, 0, 0],  # Row 3
          [4, 5, 0, 3, 0, 0],  # Row 4
          [0, 0, 1, 0, 6, 0]]  # Row 5

board3 = [[0, 6, 0, 3, 5, 0],  # Row 0
          [3, 4, 5, 0, 0, 0],  # Row 1
          [5, 1, 6, 3, 0, 3],  # Row 2
          [0, 0, 0, 5, 1, 0],  # Row 3
          [4, 0, 1, 6, 0, 5],  # Row 4
          [6, 0, 3, 4, 2, 1]]  # Row 5

boards = [board1, board2, board3]

# Function for selecting a random board
def get_board():
    length = len(boards)
    random_board_number = random.randrange(length)
    board = boards[random_board_number]

    return board

# Function for getting Assignment 2 board
def get_noroff_board():
    board = board1
    return board










