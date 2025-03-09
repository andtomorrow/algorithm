from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    input_name = stdin.readline().strip()
    print(input_name.lower())
