a, b = map(int, input().split())

def RCP(a, b): # a, b 는 1, 2, 3 중 하나
    if abs(a - b) == 0:
        winner = None
    elif abs(a - b) == 1:
        winner = max(a, b)
    elif abs(a - b) == 2:
        winner = min(a, b)
    print('A' if winner == a else 'B')

RCP(a, b)