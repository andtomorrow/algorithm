from sys import stdin
import datetime

B_YEAR, B_MONTH, B_DAY = map(int, stdin.readline().split())

C_YEAR, C_MONTH, C_DAY = map(int, stdin.readline().split())

if datetime.date(B_YEAR, C_MONTH, C_DAY) >= datetime.date(B_YEAR, B_MONTH, B_DAY):
    age_full = C_YEAR - B_YEAR
else:
    age_full = C_YEAR - B_YEAR - 1

print(age_full)

age_korean = C_YEAR - B_YEAR + 1

print(age_korean)

age_yearly = C_YEAR - B_YEAR

print(age_yearly)
