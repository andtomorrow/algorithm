from sys import stdin

while True:
    input_line = stdin.readline().strip()
    if input_line == "END":
        break
    print(input_line[::-1])
    