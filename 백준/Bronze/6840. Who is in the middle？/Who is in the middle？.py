from sys import stdin

first = int(stdin.readline())
second = int(stdin.readline())
third = int(stdin.readline())

sorted_list = sorted([first, second, third])
print(sorted_list[1])