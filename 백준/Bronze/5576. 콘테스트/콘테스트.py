W_univ = []
K_univ = []

for _ in range(10):
    W_univ.append(int(input()))

for _ in range(10):
    K_univ.append(int(input()))

print(sum(sorted(W_univ, reverse=True)[:3]), sum(sorted(K_univ, reverse=True)[:3]))