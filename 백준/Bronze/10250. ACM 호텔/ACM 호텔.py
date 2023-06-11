import sys

T = int(sys.stdin.readline())

for case in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    quotient, remainder = divmod(N, H)
    X = quotient + 1  # 몫
    Y = remainder  # 나머지  # 나머지가 0: 꼭대기층!!
    
    if Y == 0:
        y = str(H)
        X -= 1
    else:
        y = str(remainder)

    if X <= 9:
        x = '0' + str(X)
    else:
        x = str(X)
    
    print(y, x, sep="")