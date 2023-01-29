import sys, heapq

f = sys.stdin

N = int(f.readline())
array = []

for n in range(N):
    num = int(f.readline())

    if num:
        heapq.heappush(array, (abs(num), num))
    else:
        if len(array) == 0:
            print(0)
        else:
            picked = heapq.heappop(array)
            print(picked[1])