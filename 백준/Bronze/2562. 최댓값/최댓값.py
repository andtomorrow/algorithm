N = 9

nums = {}
for cycl in range(N):
    nums[cycl] = int(input())

biggest = max(nums.values())
for k, v in nums.items():
    if v == biggest:
        bggst_idx = k
        break
print(biggest, bggst_idx+1)
