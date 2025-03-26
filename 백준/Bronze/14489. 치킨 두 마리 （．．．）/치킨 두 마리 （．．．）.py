from sys import stdin

A, B = map(int, stdin.readline().split())  # 통장 두 개 잔고

C = int(stdin.readline())  # 한 마리 가격

current_cash = A + B

if current_cash - (2 * C) >= 0:
    print(current_cash - (2 * C))
else:
    print(current_cash)
