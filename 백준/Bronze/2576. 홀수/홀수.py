T = 7
odd_nums = []

for t in range(1, T+1):
    t_num = int(input())
    if t_num % 2 == 1:
        odd_nums.append(t_num)

if len(odd_nums):
    print(sum(odd_nums), min(odd_nums), sep='\n')
else:
    print(-1)