from sys import stdin

A, B = map(int, stdin.readline().split())
C, D = map(int, stdin.readline().split())

print(min((B + C), (A + D)))
