from sys import stdin
from collections import deque

num_vertex, num_node, start = map(int, stdin.readline().split())

graph = [[] for _ in range(num_vertex + 1)]

for _ in range(num_node):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for edges in graph:
    edges.sort()

visited = [False] * (num_vertex + 1)


def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for u in graph[v]:
        if not visited[u]:
            dfs(u)


dfs(start)

visited = [False] * (num_vertex + 1)
print()


def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for u in graph[node]:
            if not visited[u]:
                visited[u] = True
                queue.append(u)

bfs(start)