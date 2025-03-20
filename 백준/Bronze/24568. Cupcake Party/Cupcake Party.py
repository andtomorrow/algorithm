from sys import stdin

REGULAR_SIZE = 8
SMALL_SIZE = 3

NUM_STUDENTS = 28

num_regular_box = int(stdin.readline())
num_small_box = int(stdin.readline())

num_left_over = num_regular_box * 8 + num_small_box * 3 - NUM_STUDENTS
print(num_left_over)
