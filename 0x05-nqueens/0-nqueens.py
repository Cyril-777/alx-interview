#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard. Write a program that solves the N queens problem.
"""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[x][y]"""
    # Check the column on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower left diagonal
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """Use backtracking to find all solutions"""
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(col):
        """Recursive backtracking function"""
        if col == n:
            solution = []
            for row in range(n):
                for c in range(n):
                    if board[row][c] == 1:
                        solution.append([row, c])
            solutions.append(solution)
            return
        for row in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(col + 1)
                board[row][col] = 0

    solve(0)

    return solutions


if __name__ == "__main__":
    """Read size of board from standard input"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(n)

    def sort_solution(solution):
        # Sort the solution based on the position of queens in the first row
        return [x[1] for x in solution]

    solutions.sort(key=sort_solution)

    for solution in solutions:
        print(solution)
