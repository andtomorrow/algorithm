def grade_to_score(grade_char):
    switcher = {
        'A':4,
        'B':3,
        'C':2,
        'D':1
    }
    return switcher.get(grade_char)

def plus_minus(sign):
    switcher = {
        '+':0.3,
        '0':0.0,
        '-':-0.3
    }
    return switcher.get(sign)

score_C = input()
grd_char_c = score_C[0]
if grd_char_c == 'F':
    grade_C = 0.0
else:
    grade_C = grade_to_score(grd_char_c) + plus_minus(score_C[1])
print(grade_C)