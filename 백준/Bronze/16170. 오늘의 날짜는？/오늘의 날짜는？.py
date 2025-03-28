import datetime

utc_today = datetime.datetime.now(datetime.timezone.utc)

print(utc_today.strftime("%Y\n%m\n%d"))