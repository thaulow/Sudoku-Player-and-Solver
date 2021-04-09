# Assessment 2 @ Noroff University College
_author_ = "Thomas Thaulow"
_copyright = "Thomas Thaulow"
_email_ = "thaulow@thaulow.co"
import time
class sudoku_solver:

    def __init__(self, field):
        self.field = field
        print("The provided grid is: ")
        self.print_grid(field)
        print("\n")

    # STYLE BOARD IN TERMINAL
    def print_grid(self, field):

        for row in range(len(field)):
            if row % 2 == 0:
                print("-------+-------")

            for column in range(len(field[0])):
                if column % 3 == 0 and column != 0:
                    print(" | ", end="")

                if column == 5:
                    print(field[row][column])
                else:
                    print(str(field[row][column]) + " ", end="")

    # FIND NEXT EMPTY FIELD
    """ This function will return the position of the next empty field """
    """ or if there is none, it will return empty, meaning the Sudoku is completed """

    def find_next(self, field):

        for row in range(len(field)):
            for col in range(len(field[row])):
                if field[row][col] == 0:
                    return row, col

        return None

    def row_match(self, field, num, pos):

        empty_cell_row_position = pos[0]

        for col in range(len(field[0])):
            if field[empty_cell_row_position][col] == num:
                return False

        return True

    def col_match(self, field, num, pos):

        empty_cell_col_position = pos[1]

        for row in range(len(field)):
            if field[row][empty_cell_col_position] == num:
                return False

        return True

    def sector_match(self, field, num, pos):

        row_position = pos[0]
        col_position = pos[1]

        row_position_of_box = row_position // 2  # will always return 0, 1, or 2
        col_position_of_box = col_position // 3  # will always return 0 or 1

        """ Multiplying with 2 and 3 may takes the number larger then 6.
         Due to our loop, the excess range will be truncated """
        for row in range(row_position_of_box * 2, row_position_of_box * 2 + 2):
            for col in range(col_position_of_box * 3, col_position_of_box * 3 + 3):

                print(f"I am currently checking (row, col): {(row, col)}")

                if field[row][col] == num:
                    return False

        return True

    # OUTER/MAPPED FUNCTION VALIDATING IF NUMBERS EXIST
    def is_position_valid(self, field, num, pos):

        if self.row_match(field, num, pos):
            if self.col_match(field, num , pos):
                if self.sector_match(field, num, pos):
                    return True

                return False
            return False
        return False

    def solve(self):
        start = time.time()
        field = self.field

        # if it does not find an empty field, the Sudoku is solved,
        # and it will return True and end the function

        find = self.find_next(field)
        if not find:
            print("The solved grid is:\n")
            self.print_grid(field)
            print("Sudoku solved in", time.time() - start, "seconds")
            return True
        else:
            row, column = find

        for number_to_insert in range(1, 7):

            if self.is_position_valid(field, number_to_insert, (row, column)):

                # if the number is valid, it is added

                field[row][column] = number_to_insert

                # This is recursion, calling the same function.
                # But this time, the field changes because we added a new number.

                if self.solve():
                    return True

                field[row][column] = 0

        return False

