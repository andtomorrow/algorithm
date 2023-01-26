import sys

N = int(sys.stdin.readline())
points = []

for n in range(N):
    pnt = list(map(int, sys.stdin.readline().split()))
    points.append(pnt)

points.sort()

for p in points:
    print(*p)