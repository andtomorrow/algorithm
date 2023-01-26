N = int(input())

scores = list(map(int, input().split()))

avg = sum(scores) / len(scores)

modified_avg = (avg / max(scores)) * 100

print(modified_avg)
