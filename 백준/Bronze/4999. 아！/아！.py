from sys import stdin

him = stdin.readline().strip()
hospital = stdin.readline().strip()

his = him.count("a")
its = hospital.count("a")

if his >= its:
    print("go")
else:
    print("no")
