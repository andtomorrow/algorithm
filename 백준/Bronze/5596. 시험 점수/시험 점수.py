from sys import stdin

mingook = sum(map(int, stdin.readline().split()))
mansee = sum(map(int, stdin.readline().split()))

if mingook >= mansee:
    print(mingook)
else:
    print(mansee)