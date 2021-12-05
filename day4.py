import numpy as np


class Board:
    def __init__(self, rows, numbers):
        self.rows = np.array([np.array(row) for row in rows])
        self.numbers = numbers
        self.winning_turn = None
        self.winning_score = 0

    def play(self):
        for turn, number in enumerate(self.numbers, 1):
            for i, row in enumerate(self.rows):
                if number in row:
                    row = np.where(row == number, 'X', row)
                    self.rows[i] = row

            if self.is_bingo():
                self.winning_turn = turn
                self.winning_score = self.calculate_score(number)
                break

    def is_bingo(self):
        for row in self.rows:
            if list(row) == ['X', 'X', 'X', 'X', 'X']:
                return True
        for column in range(0, 5):
            if [row[column] for row in self.rows] == ['X', 'X', 'X', 'X', 'X']:
                return True

        return False

    def calculate_score(self, number):
        total = 0
        for row in self.rows:
            for val in row:
                if val != 'X':
                    total += int(val)

        return total * int(number)

    def __str__(self):
        return str(self.rows)

    def __repr__(self):
        return str(self)


def make_boards(board_input, numbers):
    boards = []
    rows = []

    for row in board_input:
        if row == "":
            board = Board(rows, numbers)
            boards.append(board)
            rows = []
            continue

        rows.append([x.strip() for x in row.split(' ') if x != ''])

        if row == board_input[-1]:
            board = Board(rows, numbers)
            boards.append(board)

    return boards


def main():
    with open('day4.txt') as f:
        puzzle_input = [x.strip() for x in f.readlines()]

    numbers = [x for x in puzzle_input[0].split(',')]
    boards = make_boards(puzzle_input[2:], numbers)

    for board in boards:
        board.play()

    winning_board = boards[0]
    worst_board = boards[0]
    for board in boards:
        if board.winning_turn < winning_board.winning_turn:
            winning_board = board
        if board.winning_turn > worst_board.winning_turn:
            worst_board = board

    print(winning_board.winning_score)
    print(worst_board.winning_score)


if __name__ == '__main__':
    main()
