from sys import stdin

n_of_datasets = int(stdin.readline())

for _ in range(n_of_datasets):
    eats, requires = map(int, stdin.readline().split())
    if eats >= requires:
        print("MMM BRAINS")
    else:
        print("NO BRAINS")
