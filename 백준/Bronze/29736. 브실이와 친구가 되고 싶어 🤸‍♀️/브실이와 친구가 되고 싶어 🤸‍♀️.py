from sys import stdin

A, B = map(int, stdin.readline().split())

K, X = map(int, stdin.readline().split())


candidates_int = range(A, B + 1)

num_friends = 0

for candidate_int in candidates_int:
    if abs(K - candidate_int) <= X:
        num_friends += 1

if num_friends == 0:
    print("IMPOSSIBLE")
else:
    print(num_friends)
