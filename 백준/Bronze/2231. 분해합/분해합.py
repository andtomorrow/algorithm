"""
자연수 N에 대하여, 분해합: N과 N 각 자리수의 합
예) 245의 분해합은 256 (=245+2+4+5)
-생성자 (245는 256의 생성자. 생성자가 없는 경우도, 여러 개인 경우도 있음)
구: 주어진 자연수 N의 가장 작은 생성자
"""

N = int(input())

# N의 생성자 중 가장 작은 것을 구해야 함


for num in range(max(1, N - 9 * len(str(N))), N + 1):
    if num + sum(map(int, str(num))) == N:
        print(num)
        break
else:
    print(0)
