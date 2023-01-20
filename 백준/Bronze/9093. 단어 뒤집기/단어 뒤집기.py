T = int(input())

for t in range(1, T+1):
    usr_input = input().split()
    for word in usr_input:
        print(word[::-1], end=' ')
    print()