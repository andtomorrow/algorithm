from sys import stdin

travel_time = 0

travel_time += int(stdin.readline())

travel_time += int(stdin.readline())

travel_time += int(stdin.readline())

travel_time += int(stdin.readline())


x = travel_time // 60

y = travel_time % 60

print(x)

print(y)