from sys import stdin

T = int(input())

for _ in range(T):
    R_str, S = stdin.readline().split()
    R = int(R_str)
    P = ""

    for char in S:
        P += char * R

    print(P)
