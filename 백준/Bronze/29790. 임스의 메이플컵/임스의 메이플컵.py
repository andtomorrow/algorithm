from sys import stdin

N, U, L = map(int, stdin.readline().split())

if N < 1000:
    print("Bad")

else:
    if U >= 8000:
        print("Very Good")
    elif L >= 260:
        print("Very Good")
    else:
        print("Good")
