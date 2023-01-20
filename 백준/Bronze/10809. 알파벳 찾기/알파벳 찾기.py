import collections, string

S = input()

alphabet = list(string.ascii_lowercase)
alp_idx = {}

for ltr in alphabet:
    alp_idx[ltr] = -1

for i in range(len(S)):
    if alp_idx[S[i]] == -1:
        alp_idx[S[i]] = i

print(*alp_idx.values())