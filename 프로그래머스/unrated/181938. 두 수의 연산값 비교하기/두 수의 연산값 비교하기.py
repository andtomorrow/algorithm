def solution(a, b):
    
    a_and_b = int(str(a) + str(b))
    
    a_b_2_by = 2*a*b
    
    answer = max(a_and_b, a_b_2_by)
    return answer