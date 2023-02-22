N = int(input())
etoile = '*'
for i in range(1, N+1):
    print(' ' * (N-i), etoile * (2*i - 1), sep='')