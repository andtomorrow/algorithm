"""
라인 넘버 -> 가입한 순서
정렬 규칙: 나이(증가순), 나이 같으면 가입 순서(먼저 가입 우선)
"""

N = int(input())

# sort_by_age_dict = dict.fromkeys([str(num) for num in range(1, 201)], [])

sort_by_age_dict = {str(num): [] for num in range(1, 201)}


for i in range(N):
    inpt_age_str, inpt_name = input().split()
    sort_by_age_dict[inpt_age_str].append((i, inpt_name))

for k, v in sort_by_age_dict.items():
    if v != []:
        same_age = sorted(v, key=lambda person: person[0])
        for person in same_age:
            print(f"{k} {person[1]}")
