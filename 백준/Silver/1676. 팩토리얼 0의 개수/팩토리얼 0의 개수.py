import sys
import math

N = int(sys.stdin.readline())

rev_fac = str(math.factorial(N))[::-1]
i = 0
while True:
    if rev_fac[i] != "0":
        print(i)
        break
    else:
        i += 1