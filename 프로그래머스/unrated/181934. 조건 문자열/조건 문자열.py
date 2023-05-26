def solution(ineq, eq, n, m):
    if n > m:
        if ineq == '<':
            return 0
    elif n < m:
        if ineq == '>':
            return 0
    elif n == m:
        if eq == '!':
            return 0

    return 1