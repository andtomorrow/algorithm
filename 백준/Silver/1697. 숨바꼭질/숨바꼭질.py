from collections import deque

"""
현재 수빈: N 동생: K
이동: -1, +1, *2
"""

subin, younger = map(int, input().split())

MAX = 100001
visited = [-1] * MAX

# MOVES = ["-1", "+1", "*2"]


def bfs(start: int) -> any:
    queue = deque([start])

    position = start
    visited[start] = 0

    while queue:
        position = queue.popleft()

        for operation_result in [position-1, position+1, position*2]:
            new_position = operation_result

            if 0 <= new_position < MAX:
                if visited[new_position] == -1:
                    visited[new_position] = visited[position] + 1
                    queue.append(new_position)


bfs(subin)

print(visited[younger])
