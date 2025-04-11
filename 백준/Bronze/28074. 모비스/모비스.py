from sys import stdin

MOBIS_str = "MOBIS"

input_str = stdin.readline().strip()

input_char_lst = []

for i, char in enumerate(input_str):
    input_char_lst.append(char)

success = True

for char in MOBIS_str:
    if char in input_char_lst:
        continue
    else:
        print("NO")
        success = False
        break

if success:
    print("YES")
