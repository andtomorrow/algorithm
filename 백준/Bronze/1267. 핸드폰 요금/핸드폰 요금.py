import sys

N = int(sys.stdin.readline())

calls_s = list(map(int, sys.stdin.readline().split()))

Y = 0
M = 0

for call_s in calls_s:
    yy = divmod(call_s, 30)
    mm = divmod(call_s, 60)
    Y += yy[0] * 10 + 10
    M += mm[0] * 15 + 15

if Y > M:
    print(f"M {M}")
elif Y == M:
    print(f"Y M {Y}")
elif Y < M:
    print(f"Y {Y}")
