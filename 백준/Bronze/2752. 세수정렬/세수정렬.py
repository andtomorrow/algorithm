from sys import stdin


three_nums = list(map(int, stdin.readline().split()))

result = sorted(three_nums, reverse=False)

print(*result)