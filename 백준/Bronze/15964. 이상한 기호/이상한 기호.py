def arobase(a, b):
    return (a+b)*(a-b)

A, B = map(int, input().split())
print(arobase(A, B))