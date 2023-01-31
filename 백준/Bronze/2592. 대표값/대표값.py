nums = {}

for _ in range(10):
    N = int(input())
    if N not in nums:
        nums[N] = 1
    else:
        nums[N] += 1

nums_list_prep = nums.items()
nums_list = [elm[0]*elm[1] for elm in nums_list_prep]

print(sum(nums_list) // 10)
print(sorted(nums.keys(), key=lambda k: nums[k], reverse=True)[0])