import string
from sys import stdin


S = stdin.readline().strip()

a_to_z = string.ascii_lowercase

output = []


for char in a_to_z:
    output.append(S.count(char))


print(*output, sep=" ")
