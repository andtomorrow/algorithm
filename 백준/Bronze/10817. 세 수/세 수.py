A, B, C = map(int, input().split())

nums = [A, B, C]

nums.sort()
nums.pop(0)

print(nums[0])
