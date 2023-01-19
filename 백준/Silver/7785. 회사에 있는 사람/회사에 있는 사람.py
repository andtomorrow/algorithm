import sys
present = {}

n = int(input())
for l in range(n):
    member_name, member_status = sys.stdin.readline().split()
    if member_status == 'enter':
        present[member_name] = 1
    elif member_status == 'leave':
        present[member_name] = 0

prs_members_list = []

for k, v in present.items():
    if v == 1:
        prs_members_list.append(k)
        
print(*sorted(prs_members_list, reverse=True), sep='\n')