from sys import stdin

while True:
    A, B = map(int, stdin.readline().split())
    if A == B == 0:
        break
    if A > B:
        print("Yes")
    else:
        print("No")
