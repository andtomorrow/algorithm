from sys import stdin

KING = 1
QUEEN = 1
ROOKS = 2
BISHOPS = 2
KNIGHTS = 2
PAWNS = 8

chess_pieces = [KING, QUEEN, ROOKS, BISHOPS, KNIGHTS, PAWNS]

current_nums = list(map(int, stdin.readline().split()))

needed = [chess_pieces[i] - current_nums[i] for i in range(6)]

print(*needed)
