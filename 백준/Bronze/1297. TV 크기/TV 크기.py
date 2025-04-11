from sys import stdin
import math

D, H, W = map(int, stdin.readline().split())

k = D / math.sqrt(H**2 + W**2)

height, width = math.floor(k * H), math.floor(k * W)

print(height, width)
