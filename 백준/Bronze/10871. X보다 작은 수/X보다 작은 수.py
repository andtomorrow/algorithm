N, X = map(int, (input().split()))
t_nums = map(int, input().split())

small_nums = [n for n in t_nums if n < X]
print(*small_nums)