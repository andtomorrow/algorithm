A, B, V = map(int, input().split())

night = 0
meters = 0

A + night * (A-B) >= V

night_minus_1, remainder = divmod(V-A, A-B)

if remainder == 0:
    print(night_minus_1 + 1)
else:
    print(night_minus_1 + 1 + 1)