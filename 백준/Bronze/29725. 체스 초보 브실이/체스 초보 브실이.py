from sys import stdin

chess_board = ['.'] * 8

result_score = 0

for i in range(8):
    chess_board[i] = stdin.readline().strip()
    for point in chess_board[i]:
        match point:
            case "P":
                result_score += 1
            case "p":
                result_score -= 1
            case "N":
                result_score += 3
            case "n":
                result_score -= 3
            case "B":
                result_score += 3
            case "b":
                result_score -= 3
            case "R":
                result_score += 5
            case "r":
                result_score -= 5
            case "Q":
                result_score += 9
            case "q":
                result_score -= 9

print(result_score)
