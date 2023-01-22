import sys

while True:
    usr_input = list(map(int, sys.stdin.readline().split()))
    if len(usr_input):
        A, B = usr_input
        print(A+B)
    else:
        break