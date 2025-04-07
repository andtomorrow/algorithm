import math
from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    slice_area, slice_price = map(int, stdin.readline().split())
    circular_radius, circular_price = map(int, stdin.readline().split())

    circular_area = circular_radius ** 2 * math.pi

    if slice_area / slice_price > circular_area / circular_price:
        print("Slice of pizza")
    else:
        print("Whole pizza")

