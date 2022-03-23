"""
Bingo is played on a set of boards each consisting of a 5x5 grid of numbers.
Numbers are chosen at random, and the chosen number is marked on all boards on which it appears.
(Numbers may not appear on all boards.)
If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time.
It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input).
"""

import numpy as np

with open('./inputs/bingo.txt', 'r') :
    lines = [line.strip() for line in ip.readlines()]

# print(lines)

numberList = [int(i) for i in lines[0].split(',')]  # list of numbers called
print(numberList)

boardCount = (len(lines) - 1) // 6  # each board has 6 lines (5 rows and an empty line)
print(boardCount)

boards = {}


class Board:
    def __init__(self):
        self.board = np.zeros((5, 5), dtype=int)  # for the board
        self.checked = np.zeros((5, 5), dtype=int)  # for tracking checked numbers (0 - unchecked, 1 - checked)

    def build_board(self, entry):
        for i in range(0, 5):
            rows = [int(j) for j in entry[i].split(' ') if j != '']  # convert each entry to int and ignore whitespaces
            self.board[i] = rows

    # checks if the numbers called is present on the board
    # tracks by changing the entry in the checked list to 1
    def check_number(self, n):
        if n in self.board:
            coordinates = np.where(self.board == n)
            self.checked[coordinates[0], coordinates[1]] = 1

    # checks if the current board won (any row or column is checked)
    def bingo(self):
        return self.checked.all(axis=0).any() or self.checked.all(axis=1).any()

    # gets the score of the current board
    def get_score(self, num):
        return (self.board * (self.checked == 0)).sum() * num


for val in range(0, boardCount):
    boards[val] = Board()
    # offset of 2 because of ignoring the first 2 lines
    # the end is after 5 lines
    boards[val].build_board(lines[(2 + val * 6):(7 + (val + 1) * 6)])


# checks if the board is the first win
def winner(numbers, board_list):
    for num in numbers:
        for i in range(0, len(board_list)):
            boards[i].check_number(num)
            if board_list[i].bingo():
                print("Board won: " + str([i + 1]))
                return [i, num]     # returns the number and its index


# finds the board that wins the last
def last_winner(numbers, board_list):
    winning_boards = []
    winning_number = 0

    # calculates the order in which each board wins
    # returns the last board to win and its corresponding winning call
    for num in numbers:
        for i in range(0, len(board_list)):
            if i not in winning_boards:
                board_list[i].check_number(num)
                if board_list[i].bingo():
                    winning_boards.append(i)
                    winning_number = num

    return [winning_boards[-1], winning_number]


# part 1
winning_entry = winner(numberList, boards)
print("Winning Score: " + str(boards[winning_entry[0]].get_score(winning_entry[1])))

# part 2
last_win = last_winner(numberList, boards)
print("Losing Score: " + str(boards[last_win[0]].get_score(last_win[1])))
