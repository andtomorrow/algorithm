from sys import stdin

n, m = map(int, stdin.readline().split())

quotient, remainder = divmod(n, m)

print(quotient, remainder, sep="\n")
