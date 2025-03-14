from sys import stdin

T = int(stdin.readline())

A, after_A = divmod(T, 300)
B, after_B = divmod(after_A, 60)
C, after_C = divmod(after_B, 10)

if after_C != 0:
    print(-1)

else:
    print(A, B, C, sep=" ")
