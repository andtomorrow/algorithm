import sys

num1, num2 = map(int, sys.stdin.readline().split())

num1_X, num1_Y = divmod(num1 -1, 4)
num2_X, num2_Y = divmod(num2 -1, 4)


dist = abs(num2_Y - num1_Y) + abs(num2_X - num1_X)

print(dist)
