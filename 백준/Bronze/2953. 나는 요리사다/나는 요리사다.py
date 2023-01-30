participants = []
for i in range(5):
    scores = sum(map(int, input().split()))
    participants.append(scores)

winner = max(participants)
print(participants.index(winner)+1, winner)