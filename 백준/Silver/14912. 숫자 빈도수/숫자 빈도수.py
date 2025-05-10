"""
1부터 n까지 차례대로 써 내려간 내용에서
숫자 d가 들어간 횟수를 카운트
"""

n, d = map(int, input().split())

d_count = 0

for num in range(1, n + 1):
    this_count = str(num).count(str(d))
    if this_count != 0:
        d_count += this_count

print(d_count)
