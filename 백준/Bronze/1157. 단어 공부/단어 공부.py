from collections import Counter
from sys import stdin

input_str = stdin.readline().strip()
input_str_lower = input_str.lower()
cnt_char = Counter(input_str_lower).most_common(2)

if len(cnt_char) == 1:
    print(cnt_char[0][0].upper())
elif cnt_char[0][1] != cnt_char[1][1]:
    print(cnt_char[0][0].upper())
else:
    print("?")