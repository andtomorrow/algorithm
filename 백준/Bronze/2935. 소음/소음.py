from sys import stdin

A = int(stdin.readline())
operator = stdin.readline().strip()
B = int(stdin.readline())

print(eval(f"{A} {operator} {B}"))
