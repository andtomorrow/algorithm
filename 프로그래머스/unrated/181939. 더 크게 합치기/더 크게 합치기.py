def solution(a, b):
    candidate1 = int(str(a) + str(b))
    candidate2 = int(str(b) + str(a))

    answer = max(candidate1, candidate2)

    return answer