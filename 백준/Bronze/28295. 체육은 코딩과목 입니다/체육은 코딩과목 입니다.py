from sys import stdin

DIRECTIONS = ["N", "E", "S", "W"]

"""
1: 우향우
2: 뒤로돌아
3: 좌향좌
"""

dir_idx = 0

for _ in range(10):
    cmd = stdin.readline().strip()

    match cmd:
        case "1":
            dir_idx = (dir_idx + 1) % 4
        case "2":
            dir_idx = (dir_idx + 2) % 4
        case "3":
            dir_idx = (dir_idx - 1 + 4) % 4

print(DIRECTIONS[dir_idx])
