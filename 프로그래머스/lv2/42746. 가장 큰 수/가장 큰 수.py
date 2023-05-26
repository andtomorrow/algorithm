import itertools

def solution(numbers):
    
    nums_sorted = sorted(numbers, key=lambda x: str(x)*3, reverse=True)  # 사전식 비교
    answer = "".join(map(str, nums_sorted))
    if answer[0] == '0':
        return '0'
    return answer