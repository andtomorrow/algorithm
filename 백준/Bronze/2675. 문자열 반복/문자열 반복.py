T = int(input())
for t in range(1, T+1):
    R, S = input().split()
    R = int(R)
    for char in S:
        print(char*R, sep='', end='')
    print()
