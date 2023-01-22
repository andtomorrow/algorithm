import sys, collections

stdnts = collections.defaultdict.fromkeys(range(1,31), 0)

submit = list(map(int, sys.stdin.readlines()))

for num in submit:
    stdnts[num] += 1

grad_candidates = [num for num in stdnts.keys() if stdnts[num] == 0]

print(*grad_candidates, sep='\n')