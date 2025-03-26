from sys import stdin

A = int(stdin.readline())
B = int(stdin.readline())
C = int(stdin.readline())
D = int(stdin.readline())
E = int(stdin.readline())

current_temp = A

cook_duration = 0

if current_temp < 0:
    cook_duration += abs(current_temp) * C
    current_temp = 0

if current_temp == 0:
    cook_duration += D

if current_temp >= 0:
    cook_duration += (B - current_temp) * E

print(cook_duration)
