from sys import stdin

total_on_white = 0

for i in range(8):  # 짝수행부터, 행 하나씩
    input_line = stdin.readline().strip()

    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0:  # 짝수열
                if input_line[j] == "F":
                    total_on_white += 1
    else:
        for j in range(8):
            if j % 2 == 1:  # 홀수열
                if input_line[j] == "F":
                    total_on_white += 1

print(total_on_white)
