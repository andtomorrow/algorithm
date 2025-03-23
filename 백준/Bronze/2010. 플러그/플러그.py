from sys import stdin

N = int(stdin.readline())

power_available = 0

for i in range(N):
    pow = int(stdin.readline()) - 1
    power_available += pow

power_available += 1
print(power_available)
