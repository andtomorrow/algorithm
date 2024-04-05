from sys import stdin

while True:
    M, F = map(int, stdin.readline().split())
    if M == F == 0:
        break
    print(M+F)