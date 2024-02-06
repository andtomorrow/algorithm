from sys import stdin

T = int(stdin.readline())

array = []
for i in range(T):
    array = list(map(int, stdin.readline().split()))
    print(sorted(array, reverse=True)[2])