import itertools
from sys import stdin

N = int(stdin.readline())

if N == 1:
    print(0)
else:
    print(len(list(itertools.permutations(range(N), 2))))
