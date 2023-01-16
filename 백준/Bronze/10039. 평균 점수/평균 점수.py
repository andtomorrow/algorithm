total_score = 0
for t in range(5):
    score = int(input())
    if score < 40:
        score = 40
    total_score += score
avg = int(total_score / 5)
print(avg)