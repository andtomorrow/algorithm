import sys

start_num, end_num = map(int, sys.stdin.readline().split())


def num_length_in_and_sum_out(n: int) -> int:
    """
    position: index num
    cur_num: current number
    """
    position = 0
    cur_num = 0
    somme = 0
    # while pointer < n:
    #     pointer += 1
    #     somme += pointer ^ 2
    while position < n:
        for _ in range(cur_num):
            somme += cur_num
            position += 1
            if position >= n:
                break
        cur_num += 1

    return somme


result = num_length_in_and_sum_out(
    end_num) - num_length_in_and_sum_out(start_num - 1)

print(result)
