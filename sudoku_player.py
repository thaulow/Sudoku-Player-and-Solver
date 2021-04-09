# Assessment 2 @ Noroff University College
_author_ = "Thomas Thaulow"
_copyright = "Thomas Thaulow"
_email_ = "thaulow@thaulow.co"
import time
class sudoku_player:

    def __init__(self, field):
        self.field = field
        print("The provided grid is: ")
        self.fixed_pos = self.fixed_positions(field)

    def fixed_positions(self, field):

        points = []
        for row in range(len(field)):
            for col in range(len(field[row])):
                if field[row][col] != 0:
                    point = [row, col]
                    points.append(point)

        # return list of fixed points
        return points

    def print_grid(self, field):

        for row in range(len(field)):
            if row % 2 == 0:
                print("-------+-------")

            for col in range(len(field[row])):
                if col % 3 == 0 and col != 0:
                    print(" | ", end="")

                if col == 5:
                    print(field[row][col])
                else:
                    print(str(field[row][col]) + " ", end="")

    # CHECK IF POSITION IS VALID
    """ This function will match the current position, with the list of positions thats
    not allowed to be edited """

    def row_match(self, field, num, pos):
        row = pos[0]
        print("validating row: ")
        match = False
        for counter in field[row]:
            if num == counter:
                match = True
                print(f"Number {num} exist in row: {row + 1}")
                break
            else:
                match = False

        print(f"Does number exist in row: {match}")
        return match

    def column_match(self, field, num, pos):
        col = pos[1]
        print("Validating column: ")
        match = False
        for counter in range(len(field)):
            if field[counter][col] == num:
                match = True
                print(f"Number {num} exist in row: {col + 1}")
                break
            else:
                match = False

        print(f"Does number exist in column: {match}")
        return match

    def sector_match(self, field, num, pos):
        match = False
        row = pos[0]
        col = pos[1]

        row_position_of_box = row // 2  # will always return 0, 1, or 2
        col_position_of_box = col // 3  # will always return 0 or 1

        for i in range(row_position_of_box * 2, row_position_of_box * 2 + 2):
            for j in range(col_position_of_box * 3, col_position_of_box * 3 + 3):

                print(f"Number being checked: {(i, j)}")

                if field[i][j] == num:
                    print("number match")
                    match = True
                    return match

        print(f"Does number match in sector {match} ")
        return match

    def is_position_valid(self, field, num, pos):
        if not self.row_match(field, num, pos):
            if not self.column_match(field, num, pos):
                if not self.sector_match(field, num, pos):
                    return True

                return False
            return False
        return False

    # CHECK IF NUMBER IS UNIQUE
    """ This function and the 2 others underneath will check if the current number
       is found in a row, column or sector """
    def is_row_complete(self, field, num, row):
        print("checking row")
        occurrence = 0
        for col in range(len(field[row])):
            if field[row][col] == num:
                occurrence += 1

        if occurrence > 1:
            print("Number occurred more than once in a row")
            print(f"Number {num} is not valid in the row at position {(row + 1, col + 1)}")
            return False
        else:
            print("Number occurred once")
            return True

    def is_col_complete(self, field, num, col):
        print("checking column")
        occurrence = 0

        for row in range(len(field)):
            if field[row][col] == num:
                occurrence += 1

        if occurrence > 1:
            print(f"Number {num} not valid in the col at position {(row + 1, col + 1)}")
            return False
        else:
            return True

    def is_sector_complete(self, field, num, pos):
        occurrence = 0
        row = pos[0]
        col = pos[1]

        box_row = row // 2  # will always return 0, 1, or 2
        box_col = col // 3  # will always return 0 or 1

        for row in range(box_row * 2, box_row * 2 + 2):  # for rows
            for col in range(box_col * 3, box_col * 3 + 3):  # for columns
                if field[row][col] == num:
                    occurrence += 1

        if occurrence > 1:
            print(f"Number {num} not valid at in box at position {(row + 1, col + 1)}")
            return False
        else:
            return True

    def is_solved(self, field):
        for row in range(len(field)):
            for col in range(len(field[row])):

                num = field[row][col]

                if num == 0:
                    return False
                else:
                    if self.is_row_complete(field, num, row):
                        if self.is_col_complete(field, num, col):
                            if self.is_sector_complete(field, num, (row, col)):
                                continue

                            return False
                        return False
                    return False

        return True

    def start_playing(self):
        # keeps track of number of attempts
        start = time.time()
        moves = 0
        field = self.field
        while not self.is_solved(field):

            self.print_grid(field)

            moves += 1
            while True:
                try:
                    number_to_insert = int(input("Enter number to add: "))
                    row = int(input("Enter row: "))
                    col = int(input("Enter column: "))
                    row -= 1
                    col -= 1
                except ValueError:
                    print("Sorry, invalid input. Please try again...")
                    continue
                else:
                    break

            pos = [row, col]

            if pos in self.fixed_pos:
                print(f"This position has fixed value of {field[row][col]}")
                self.print_grid(field)
                continue

            if self.is_position_valid(field, number_to_insert, (row, col)):
                field[row][col] = number_to_insert

                self.print_grid(field)

        else:
            print(f"Congratulations! You solved the Soduko!......Number of moves: {moves} ")
            print("Sudoku solved in", time.time() - start, "seconds")
            return
