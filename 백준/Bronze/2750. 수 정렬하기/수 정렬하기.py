N = int(input())
nums = []
for cycle in range(N):
    nums.append(int(input()))
nums = sorted(nums)
for n in nums:
    print(n)