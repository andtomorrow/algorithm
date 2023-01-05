import datetime as dt
timeoffset = dt.timezone(dt.timedelta(hours=7))

here = dt.datetime.now(timeoffset)

print(here.strftime('%Y-%m-%d'))