import datetime as dt
H, M = map(int, input().split())

sang = dt.datetime.strptime(f"{H}:{M}", "%H:%M")

timeoffset = dt.timedelta(minutes=-45)

chang = sang + timeoffset

print(*chang.timetuple()[3:5])