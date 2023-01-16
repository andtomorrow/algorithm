T = int(input())
for t in range(1, T+1):
    case_num = f'Case #{t}:'
    print(case_num, sum(map(int, input().split())))