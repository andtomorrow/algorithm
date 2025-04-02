from sys import stdin

while True:
    B, N = map(int, stdin.readline().split())

    if B == N == 0:
        break

    a_candidate = 1

    while a_candidate ** N <= B:
        a_candidate += 1

    if abs(B - a_candidate ** N) >= abs(B - (a_candidate - 1) ** N):
        print(a_candidate - 1)
    else:
        print(a_candidate)
