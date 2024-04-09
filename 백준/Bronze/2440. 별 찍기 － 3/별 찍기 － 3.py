from sys import stdin

N = int(stdin.readline())

num_of_stars = N

for _ in range(N):
    print("*" * num_of_stars)
    num_of_stars -= 1