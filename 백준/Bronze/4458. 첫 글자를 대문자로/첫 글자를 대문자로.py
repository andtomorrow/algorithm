from sys import stdin

N = int(stdin.readline())

for _ in range(N):
    input_str = stdin.readline().strip()

    print(f"{input_str[0].upper()}{input_str[1:]}")
