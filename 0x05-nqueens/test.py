#!/usr/bin/python3
"""N queens cha;enge"""
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    stop = False

    def print_board(board):
        for row in board:
            print(''.join(row))

    def is_valid_move(board, row, col):
        n = len(board)
        if any(board[row]):
            return false
        if any([board[i][col] for i in range(n)]):
            return false
        for i in range(n):
            for j in range(n):
                if i + j == row + col or i - j == row - col:
                    if board[i][j]:
                        return False
        return true

    def solve_n_queens(n):
        board = [['.'for _ in range(n)] for _ in range(n)]
        def backtrack(row):
            if row == n:
                return True
            for col in range(n):
                if is_valid_move(board, row, col):
                    board[row][col] = 'Q'
                    if backtrack(row + 1):
                        return True
                    board[row][col] = '.'
            return False
        backtrack(0)
        print_board(board)
