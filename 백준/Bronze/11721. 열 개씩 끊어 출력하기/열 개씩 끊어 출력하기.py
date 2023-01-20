word = input()
chars_in_1_line = len(word)
if chars_in_1_line % 10 == 0:
    num_lines = chars_in_1_line // 10
else:
    num_lines = chars_in_1_line // 10 + 1

for ln in range(num_lines):
    print(*word[10 * ln: 10 * (ln + 1)], sep='')