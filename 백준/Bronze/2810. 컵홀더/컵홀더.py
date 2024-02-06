from sys import stdin

N = int(stdin.readline())

cnt = 0
row_info = stdin.readline().strip()

cnt += row_info.count("LL")
row_info.replace("LL", "")
cnt += row_info.count("S")
cnt += 1

if cnt > N:
    cnt = N

print(cnt)