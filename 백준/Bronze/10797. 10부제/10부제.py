from sys import stdin
from collections import Counter

day_num = int(stdin.readline())

lst_car_num = list(map(int, stdin.readline().split()))

cnt = Counter(lst_car_num).get(day_num)
if cnt is None:
    cnt = 0

print(cnt)
