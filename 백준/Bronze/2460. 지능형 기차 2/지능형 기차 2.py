from sys import stdin

now_onboard = 0
max_onboard = 0

for _ in range(10):
    passengers_out, passengers_in = map(int, stdin.readline().split())

    now_onboard -= passengers_out

    now_onboard += passengers_in
    if now_onboard > max_onboard:
        max_onboard = now_onboard

print(max_onboard)
