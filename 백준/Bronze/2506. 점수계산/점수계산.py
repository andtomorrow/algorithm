N = int(input())

data = map(int, input().split())
score = 0
streak = 0
for t in data:
    if t == 1:
        streak += 1
        score += streak
    else:
        streak = 0

print(score)