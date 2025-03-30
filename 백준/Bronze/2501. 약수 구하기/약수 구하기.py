from sys import stdin

N, K = map(int, stdin.readline().split())

divisors_of_N = []
for i in range(1, N+1):
    if N % i == 0:
        divisors_of_N.append(i)

if len(divisors_of_N) < K:
    print(0)
else:
    print(divisors_of_N[K - 1])
