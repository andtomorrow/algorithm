from sys import stdin

T, S = map(int, stdin.readline().split())

if T >= 12 and T <= 16:
    if S == 0:
        num_rice = 320
    else:
        num_rice = 280
else:
    num_rice = 280

print(num_rice)
