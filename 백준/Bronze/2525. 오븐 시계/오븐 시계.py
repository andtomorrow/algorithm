import datetime as dt

h, m = map(int, input().split())
curr_time = dt.datetime(year=1, month=1, day=1, hour=h, minute=m)

cook_min = int(input())
duration = dt.timedelta(minutes=cook_min)

finished = curr_time + duration

print(finished.hour, finished.minute)