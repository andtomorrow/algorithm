N = int(input())

five_by = []
five_kg_bags = 0
three_kg_bags = 0

n = 0
while 5 * n <= N:
    if (N - (5*n)) % 3 == 0:
        five_by.append(n)
    n += 1

if len(five_by) == 0:
    bags = -1
else:
    five_kg_bags = max(five_by)

    three_kg_bags = (N - (5 * five_kg_bags)) // 3
    bags = five_kg_bags + three_kg_bags

print(bags)