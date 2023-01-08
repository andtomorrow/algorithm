import sys
T = int(input())
for n in range(T):
    print(sum(map(int, sys.stdin.readline().split())))