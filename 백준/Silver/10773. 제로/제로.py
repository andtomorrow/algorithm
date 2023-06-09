import sys

K = int(sys.stdin.readline())

lifo = []

for i in range(K):
    in_num = int(sys.stdin.readline())
    if in_num != 0:
        lifo.append(in_num)
    else:
        lifo.pop()

print(sum(lifo))