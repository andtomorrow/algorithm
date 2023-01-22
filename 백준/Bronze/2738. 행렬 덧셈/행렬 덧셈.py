N, M = map(int, input().split())

A = []
B = []

for ln in range(N):
    A.append(list(map(int, input().split())))
for ln in range(N):
    B.append(list(map(int, input().split())))

new_matrix = []

for y in range(N):
    ln = []
    for x in range(M):
        somme = A[y][x]+B[y][x]
        ln.append(somme)
    new_matrix.append(ln)
    print(*new_matrix[y])