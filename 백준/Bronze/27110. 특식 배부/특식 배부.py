from sys import stdin

N = int(stdin.readline())

A, B, C = map(int, stdin.readline().split())

print(min(N, A) + min(N, B) + min(N, C))
