from sys import stdin

A, B = map(int, stdin.readline().split())

if B >= A - 1:  # 치즈가 안 모자랄 경우
    total_size = 2 * A - 1
else:  # 치즈가 모자랄 경우
    total_size = 2 * B + 1

print(total_size)
