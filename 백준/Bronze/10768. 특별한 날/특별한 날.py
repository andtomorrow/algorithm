from sys import stdin

month = int(stdin.readline())
day = int(stdin.readline())

if month > 2:
    print("After")
elif month < 2:
    print("Before")
elif month == 2:
    if day > 18:
        print("After")
    elif day == 18:
        print("Special")
    else:
        print("Before")
