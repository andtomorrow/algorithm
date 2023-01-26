N = int(input())

seat_nums = list(map(int, input().split()))
occupied = []
seated = 0

for num in seat_nums:
    if num not in occupied:
        occupied.append(num)
        seated += 1

print(len(seat_nums) - seated)