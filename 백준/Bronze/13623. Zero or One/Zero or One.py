from sys import stdin

A, B, C = map(int, stdin.readline().split())

LIST_INDEX_DICT = {0: "A", 1: "B", 2: "C"}

all_lst = [A, B, C]

cnt_zero = all_lst.count(0)
cnt_one = all_lst.count(1)

if cnt_zero == 1:
    print(LIST_INDEX_DICT[all_lst.index(0)])
elif cnt_one == 1:
    print(LIST_INDEX_DICT[all_lst.index(1)][0])
else:
    print("*")
