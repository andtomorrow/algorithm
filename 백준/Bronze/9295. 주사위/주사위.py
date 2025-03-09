from sys import stdin

T = int(stdin.readline())

for t in range(1, T+1):
    print(f"Case {t}: {sum(map(int, (stdin.readline().split())))}")
