from sys import stdin

grid_board = [None] * 9

for i in range(9):
    grid_board[i] = list(map(int, stdin.readline().split()))

max_candidate = 0

for i in range(9):
    max_compared = max(grid_board[i])
    max_candidate = max(max_candidate, max_compared)

print(max_candidate)

for i in range(9):
    if max_candidate in grid_board[i]:
        print(i+1, grid_board[i].index(max_candidate) + 1)
