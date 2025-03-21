from sys import stdin

N = int(stdin.readline())

for _ in range(N):
    input_str = stdin.readline().strip()
    if len(input_str) >= 6 and len(input_str) <= 9:
        print("yes")
    else:
        print("no")
