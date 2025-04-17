import sys

N = int(sys.stdin.readline())

count = [0] * (10000+1)

# 인덱스 값을 키처럼 활용함. 0부터 시작함에 유의.

for _ in range(N):
    inpt_num = int(sys.stdin.readline())
    count[inpt_num] += 1

for i in range(1, 10001):
    for _ in range(count[i]):
        sys.stdout.write(f"{i}\n")
