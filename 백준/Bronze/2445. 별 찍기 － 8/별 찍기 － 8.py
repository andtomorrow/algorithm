N = int(input())


for i in range(1, N):
    stars = "*" * i
    space = (2 * N - 2 * i) * " "
    print(stars, space, stars, sep="")

print("*" * 2 * N)

for i in range(1, N):
    stars = (N - i) * "*"
    space = 2 * i * " "
    print(stars, space, stars, sep="")
