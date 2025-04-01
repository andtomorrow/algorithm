from sys import stdin

N = int(stdin.readline())

plans = list(map(int, stdin.readline().split()))

total_hours = sum(plans) + 8 * (len(plans) - 1)

work_days, work_hours = divmod(total_hours, 24)

print(work_days, work_hours)
