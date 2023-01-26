nums = list(input().split())

rvsd_nums = map(int, (nums[0][::-1], nums[1][::-1]))

sangsu_answer = max(rvsd_nums)

print(sangsu_answer)