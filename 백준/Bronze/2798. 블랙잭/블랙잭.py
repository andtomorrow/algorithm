import itertools as itt

N, M = map(int, input().split())
# N, M: 5, 21

nums = map(int, input().split())
# nums = 5,6,7,8,9
picked_three = list(itt.combinations(nums, 3))
sum_three = [sum(picked_three[i]) for i in range(len(picked_three)) if sum(picked_three[i]) <= M]

print(sorted(sum_three, key=lambda val: abs(M-val))[0])