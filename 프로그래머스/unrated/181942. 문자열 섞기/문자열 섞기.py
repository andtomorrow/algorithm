def solution(str1, str2):
    answer = ''
    itr1 = iter(str1)
    itr2 = iter(str2)
    for i in range(len(str1)):
        answer += next(itr1) + next(itr2)

    return answer