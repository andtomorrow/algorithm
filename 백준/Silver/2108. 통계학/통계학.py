from sys import stdin
from collections import Counter

N = int(input())
nums = []

for _ in range(N):
    nums.append(int(stdin.readline()))

nums.sort(reverse=True)
length = len(nums)


def print_stats(nums, length):
    """
    Print avg, median, most_freq, range in each line
    """
    # print((round((sum(nums) / length)))) <- 틀림
    avg_float = sum(nums) / length
    print(int(avg_float + 0.5) if avg_float > 0 else int(avg_float - 0.5))
    print(nums[length // 2])

    # 최빈값 처리
    freq = Counter(nums)
    max_freq = max(freq.values())
    modes = [num for num, cnt in freq.items() if cnt == max_freq]
    modes.sort()
    if len(modes) > 1:
        print(modes[1])  # 두 번째로 작은 값
    else:
        print(modes[0])  # 하나뿐이면 그 값

    print(abs(max(nums) - min(nums)))


print_stats(nums, length)
