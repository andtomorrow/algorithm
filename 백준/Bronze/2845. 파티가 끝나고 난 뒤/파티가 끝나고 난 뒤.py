import sys

L, P = map(int, sys.stdin.readline().split())
journal_nums = map(int, sys.stdin.readline().split())
diff = []
for n in journal_nums:
    diff.append(n - (L * P))

print(*diff)