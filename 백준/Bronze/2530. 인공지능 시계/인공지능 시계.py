from sys import stdin

A, B, C = map(int, stdin.readline().split())

D = int(stdin.readline())

A_added, after_A = divmod(D, 60 * 60)
B_added, after_B = divmod(after_A, 60)
C_added = after_B

A = A + A_added
B = B + B_added
C = C + C_added

B_added, C = divmod(C, 60)
B += B_added
A_added, B = divmod(B, 60)
A += A_added
A %= 24

print(A, B, C, sep=" ")
