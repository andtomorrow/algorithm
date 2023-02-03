import sys, heapq as hq

input = sys.stdin.readline

N = int(input())

nums = []
for _ in range(N):
    hq.heappush(nums, int(input()))

for _ in range(N):
    print(hq.heappop(nums))