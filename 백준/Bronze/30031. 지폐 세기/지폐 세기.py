from sys import stdin

N = int(stdin.readline())

total_won = 0

for _ in range(N):
    width, height = map(int, stdin.readline().split())
    match width:
        case 136:
            total_won += 1000
        case 142:
            total_won += 5000
        case 148:
            total_won += 10000
        case 154:
            total_won += 50000

print(total_won)
