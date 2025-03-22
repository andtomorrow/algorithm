from sys import stdin

N, K = map(int, stdin.readline().split())

def get_grade(P):
    if P <= 4:
        return 1
    elif P <= 11:
        return 2
    elif P <= 23:
        return 3
    elif P <= 40:
        return 4
    elif P <= 60:
        return 5
    elif P <= 77:
        return 6
    elif P <= 89:
        return 7
    elif P <= 96:
        return 8
    else:
        return 9


percentage_lst = list(map(int, stdin.readline().split()))

print(*[get_grade((elm * 100) // N) for elm in percentage_lst])
