from sys import stdin

FIRST_TEN_STR = "9780921418"

isbn = FIRST_TEN_STR  # isbn: string

for _ in range(3):
    input_num = stdin.readline().strip()
    isbn += input_num

one_three_sum = 0

for i, digit in enumerate(isbn):
    if i % 2 == 0:
        one_three_sum += int(isbn[i]) * 1
    else:
        one_three_sum += int(isbn[i]) * 3

print(f"The 1-3-sum is {one_three_sum}")
