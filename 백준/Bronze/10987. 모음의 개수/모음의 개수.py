from sys import stdin

voyelles = 'aeiou'

input_txt = stdin.readline()

cnt_voyelles = 0

for char in input_txt:
    if char in voyelles:
        cnt_voyelles += 1

print(cnt_voyelles)
