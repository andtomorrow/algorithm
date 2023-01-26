N = int(input())
points = []

for n in range(N):
    pnt = list(map(int, input().split()))
    points.append(pnt)

points.sort()

for p in points:
    print(*p)