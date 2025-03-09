from sys import stdin

L = int(stdin.readline())
A = int(stdin.readline())
B = int(stdin.readline())
C = int(stdin.readline())
D = int(stdin.readline())

homework_days = 0
extra_day = 0

if A//C >= B//D:
    homework_days = A//C
    if A % C != 0:
        extra_day = 1
else:
    homework_days = B//D
    if B % D != 0:
        extra_day = 1

print(L - homework_days - extra_day)
