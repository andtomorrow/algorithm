from sys import stdin

N = int(stdin.readline())

for _ in range(N):
    input_name = stdin.readline().strip()

    if "S" in input_name:
        print(input_name)
        break
