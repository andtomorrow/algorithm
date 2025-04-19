from sys import stdin
import sys
sys.setrecursionlimit(10**6)

DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]

T = int(stdin.readline())

for _ in range(T):  # 밭의 너비와 배추 개수
    width, height, num_cabbage = map(int, stdin.readline().split())

    field = [[0 for _ in range(width)] for _ in range(height)]
    visited = [[False for _ in range(width)] for _ in range(height)]

    num_ver = 0

    def dfs(y, x):
        visited[y][x] = True
        for move_y, move_x in DIRECTIONS:
            new_y, new_x = y + move_y, x + move_x
            if 0 <= new_y < height and 0 <= new_x < width:
                if field[new_y][new_x] == 1 and not visited[new_y][new_x]:
                    dfs(new_y, new_x)

    for _ in range(num_cabbage):
        x, y = map(int, stdin.readline().split())

        field[y][x] = 1

    for i in range(height):
        for j in range(width):
            if field[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                num_ver += 1

    print(num_ver)
