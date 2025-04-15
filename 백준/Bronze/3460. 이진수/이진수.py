from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())

    one_position_lst = []

    reversed_bin_str_n = str(bin(n))[::-1]
    for i, char in enumerate(reversed_bin_str_n):
        if char == "1":
            one_position_lst.append(i)
        if char == "b":
            break

    print(*one_position_lst)
