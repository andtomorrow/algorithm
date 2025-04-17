from sys import stdin

current_score = 0

for _ in range(10):
    mushroom = int(stdin.readline())
    if abs(100 - current_score) >= abs(100 - (current_score + mushroom)):
        current_score += mushroom
    else:
        break

print(current_score)
