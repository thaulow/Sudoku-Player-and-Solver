# Assessment 2 @ Noroff University College
_author_ = "Thomas Thaulow"
copyright = "Thomas Thaulow"
_email_ = "thaulow@thaulow.co"

from sudoku_boards import get_board
from sudoku_boards import get_noroff_board
from sudoku_player import sudoku_player
from sudoku_solver import sudoku_solver

print("##################################")
print("#### -----------------------  ####")
print("#### Welcome to Noroff Sudoku ####")
print("#### -----------------------  ####")
print("##################################")


# Ask user for assignment board or random generated board (board class)
user_board = ""
while (user_board != "business") and (user_board != "Business") and (user_board != "pleasure") and (user_board != "Pleasure"):
    user_board = input("Business or Pleasure? (assignment 2 board or random board): ")

# If business = teacher. Teacher wants assignment 2.
if user_board == "business" or "Business":
    board = get_noroff_board()

# If pleasure = Person wants to random boards.
elif user_board == "pleasure" or "Pleasure":
    board = get_board()

# Ask user if they want to play or get it automatically solved.
user_decision = ""
while (user_decision != "play") and (user_decision != "solve"):
    user_decision = input("Do you want to play or solve it:( play/solve ): ")

# If user wants to play, run SudokuPlayer
if user_decision == "play":
    game = sudoku_player(board)
    game.start_playing()

# If user wants it solved, run SudokuSolver
elif user_decision == "solve":
    solver = sudoku_solver(board)
    solver.solve()
