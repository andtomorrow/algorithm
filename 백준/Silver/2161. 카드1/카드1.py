N = int(input())
cards = list(range(1, N+1))
ground = []

while len(cards) > 1:
    ground.append(cards.pop(0))
    cards.append(cards.pop(0))

print(*ground, *cards)