from sys import stdin
from collections import Counter

N = int(stdin.readline())

prices = []

for _ in range(N):
    personal_record = list(map(int, stdin.readline().split()))
    record_counter = Counter(personal_record)
    match len(record_counter.most_common(3)):
        case 3:
            price = max(record_counter.keys()) * 100
        case 2:
            price = record_counter.most_common(1)[0][0] * 100 + 1000
        case 1:
            price = record_counter.most_common(1)[0][0] * 1000 + 10000
    prices.append(price)

print(max(prices))
