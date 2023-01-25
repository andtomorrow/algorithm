T = int(input())

for t in range(1, T+1):
    ox_ansr = input()

    streak = 0
    score = 0
    for ansr in ox_ansr:
        if ansr == 'X':
            streak = 0
        elif ansr == 'O':
            streak += 1
            score += streak

    print(score)