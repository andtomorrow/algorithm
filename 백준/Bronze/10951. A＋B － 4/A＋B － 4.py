import sys

while True:
    nums = map(int, sys.stdin.readline().split())
    try:
        A, B = nums
        print(A+B)
    except ValueError:
        break