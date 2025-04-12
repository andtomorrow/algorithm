from sys import stdin

T = int(stdin.readline())

def triangular_num(n):
    ret_value = 0
    for i in range(1, n+1):
        ret_value += i
    return ret_value

for _ in range(T):
    n = int(stdin.readline())
    triangular_sum = 0
    for i in range(1, n+1):
        triangular_sum += i * triangular_num(i+1)

    print(triangular_sum)
