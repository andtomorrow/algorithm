N, M, K = map(int, input().split())

num_of_teams = min(N // 2, M)

# 이후 K명을 제거

num_of_remainders = N + M - 3 * num_of_teams

while num_of_remainders < K:
    num_of_teams -= 1
    num_of_remainders += 3

print(num_of_teams)
