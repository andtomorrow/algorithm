from sys import stdin

while True:
    input_str = stdin.readline().strip()
    if input_str == "0":
        break

    length = 0

    length += len(input_str) + 1

    for char in input_str:
        if char == "1":
            length += 2
        elif char == "0":
            length += 4
        else:
            length += 3

    print(length)
