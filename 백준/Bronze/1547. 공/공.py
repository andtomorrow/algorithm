M = int(input())

cup_with_ball = '1'

for _ in range(M):
    L2R, R2L = input().split()
    if L2R == R2L:
        continue
    elif L2R == cup_with_ball:
        cup_with_ball = R2L
    elif R2L == cup_with_ball:
        cup_with_ball = L2R
    else:
        continue

print(int(cup_with_ball))