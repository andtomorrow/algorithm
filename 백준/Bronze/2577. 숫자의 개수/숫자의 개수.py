from collections import Counter

"""
세 자연수 A, B, C
구: A*B*C 계산결과에서 0, 9가 각각 몇 번씩 쓰였는지
"""

A = int(input())
B = int(input())
C = int(input())


dict_zero_to_nine = dict.fromkeys('0123456789')

target_num = A * B * C

analysis = Counter(str(target_num))

dict_zero_to_nine.update(analysis)


for k, v in dict_zero_to_nine.items():
    if v is None:
        print(0)
    else:
        print(v)
