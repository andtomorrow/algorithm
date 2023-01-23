N = int(input())

for n in range(1, N+1):
    ln = str(' '*(N-n) + '*'*n)
    print(ln)