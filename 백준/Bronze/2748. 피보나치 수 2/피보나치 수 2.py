from sys import stdin

n = int(stdin.readline())

STARTING_PART = [0, 1]

def fib(n: int) -> int:

    array = STARTING_PART

    if n > 2:
        for i in range(n-1):
            array.append(sum(array[-2:]))

    return array[-1]


print(fib(n))