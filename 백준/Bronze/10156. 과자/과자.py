from sys import stdin

K, N, M = map(int, stdin.readline().split())

total_price = K * N

to_be_added = total_price - M

if to_be_added < 0:
    to_be_added = 0

print(to_be_added)
