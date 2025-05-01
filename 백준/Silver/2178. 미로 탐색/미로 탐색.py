from collections import deque

height, width = map(int, input().split())

maze = [[0 for _ in range(width)] for _ in range(height)]

for i in range(height):
    this_inpt = input()
    for j in range(width):
        maze[i][j] = int(this_inpt[j])


FOUR_DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(
        y: int, x: int
) -> any:
    queue = deque()
    queue.append((y, x))

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            new_y = y + FOUR_DIRECTIONS[i][0]
            new_x = x + FOUR_DIRECTIONS[i][1]

            if 0 <= new_y < height and 0 <= new_x < width:
                if maze[new_y][new_x] == 1:
                    maze[new_y][new_x] = maze[y][x] + 1
                    queue.append((new_y, new_x))


bfs(0, 0)

print(maze[height-1][width-1])
