from sys import stdin

N = int(stdin.readline())

idx = 0

for _ in range(N):
    idx += 1
    content = stdin.readline().replace("\n", "")
    print(f"{idx}. {content}")