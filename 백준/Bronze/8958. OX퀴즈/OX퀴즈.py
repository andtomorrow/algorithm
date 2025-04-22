T = int(input())

for _ in range(T):
    inpt_str = input()

    idx = 0
    SCORE_ZERO = 0
    current_score = SCORE_ZERO

    total_score = 0

    for char in inpt_str:
        if char == "O":
            current_score += 1
            total_score += current_score
        elif char == "X":
            current_score = SCORE_ZERO

    print(total_score)
