from sys import stdin

total_price = int(stdin.readline())
price_cal = total_price

for _ in range(9):
    price_cal -= int(stdin.readline())

print(price_cal)
