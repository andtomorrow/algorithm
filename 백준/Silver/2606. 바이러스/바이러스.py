coms_n = int(input())
connected_n = int(input())
computers = [[] * (coms_n+1) for _ in range(coms_n+1)]

for _ in range(connected_n):
    add1, add2 = map(int, input().split())
    computers[add1].append(add2)
    computers[add2].append(add1)

visited = [False] * (coms_n + 1)

def dfs(start):
    stack = [start]
    visited[start] = True
    while stack:
        cur = stack.pop()
        for adj in computers[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
    return visited

print(dfs(1).count(True) - 1)