from sys import stdin

three_of_four = []
one_of_two = []

for _ in range(4):
    three_of_four.append(int(stdin.readline()))

min_idx = three_of_four.index(min(three_of_four))
three_of_four.pop(min_idx)

for _ in range(2):
    one_of_two.append(int(stdin.readline()))

min_idx = one_of_two.index(min(one_of_two))
one_of_two.pop(min_idx)

print(sum(three_of_four) + sum(one_of_two))
