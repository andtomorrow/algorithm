T = int(input())
for t in range(1, T+1):
    case_num = f'Case #{t}:'
    A, B = map(int, input().split())
    print(case_num, A, '+', B, '=', A+B)