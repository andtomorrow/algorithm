A = range(90, 100+1)
B = range(80, 90)
C = range(70, 80)
D = range(60, 70)
F = range(0, 60)

grade_ranges = [A,B,C,D,F]
grades = ['A','B','C','D','F']

score = int(input())

for i in range(len(grade_ranges)):
    if score in grade_ranges[i]:
        grade = grades[i]
        print(grade)
        break