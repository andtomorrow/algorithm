friends = list(map(int, input().split()))

first_team = []
second_team = []

first_team.append(friends.pop(friends.index(max(friends))))
first_team.append(friends.pop(friends.index(min(friends))))
second_team = friends

print(abs(sum(first_team) - sum(second_team)))