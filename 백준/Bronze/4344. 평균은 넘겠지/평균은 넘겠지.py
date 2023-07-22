import sys

C = int(sys.stdin.readline())

for t in range(C):
    input_ln = list(map(int, sys.stdin.readline().split()))
    N = input_ln[0]
    avg = sum(input_ln[1:]) / N
    cnt_gt_avg = 0
    for num in input_ln[1:]:
        if num > avg:
            cnt_gt_avg += 1
    case_result = cnt_gt_avg / N
    print(f"{case_result:.3%}")