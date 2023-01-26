A = int(input())
B = int(input())
C = int(input())

tri_sides = [A, B, C]

if A + B + C != 180:
    tri_type = 'Error'
else:
    side_lngth = list(dict.fromkeys(tri_sides))
    if len(side_lngth) == 1:
        tri_type = 'Equilateral'
    elif len(side_lngth) == 2:
        tri_type = 'Isosceles'
    else:
        tri_type = 'Scalene'

print(tri_type)