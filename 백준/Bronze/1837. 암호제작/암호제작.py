from sys import stdin
import math

def seive_of_erastosthenes(N):
    primes = [True] * (N+1)
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(N)) + 1):
        if primes[i]:
            for j in range(i*i, N+1, i):
                primes[j] = False

    return [i for i in range(N+1) if primes[i]]


P, K = stdin.readline().split()
K = int(K)

prime_nums_lst = seive_of_erastosthenes(K-1)

def mod_large_number(P, small_prime):
    remainder = 0
    for digit in P:
        remainder = (remainder * 10 + int(digit)) % small_prime
    return remainder


found = False

for p_candidate in prime_nums_lst:
    if mod_large_number(P, p_candidate) == 0:
        print(f"BAD {p_candidate}")
        found = True
        break
else:
    print("GOOD")
