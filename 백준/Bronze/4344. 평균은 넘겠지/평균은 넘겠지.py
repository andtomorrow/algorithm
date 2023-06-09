import sys
from collections import Counter

C = int(sys.stdin.readline())
for case in range(C):
    case_in = list(map(int, sys.stdin.readline().split()))
    N, scores = case_in[0], case_in[1:]
    
    case_avg = sum(scores) / N
    cnt = Counter(scores)

    gt_avg_num = 0

    for k, v in cnt.items():
        if k > case_avg:
            gt_avg_num += v
    
    print(f'{(gt_avg_num / N):.3%}')