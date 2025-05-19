from sys import stdin

"""
공집합이 아닌 두 집합 A, B
출력: 대칭 차집합의 원소의 개수
대칭차집합 = (A-B)와 (B-A)의 합집합
"""

num_A, num_B = map(int, input().split())

A = set(map(int, stdin.readline().split()))
B = set(map(int, stdin.readline().split()))

print(len(A-B) + len(B-A))
