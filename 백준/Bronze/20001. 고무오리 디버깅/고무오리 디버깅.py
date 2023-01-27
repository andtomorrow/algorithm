start = input()

unsolved = 0

while True:
    cycl = input()
    if cycl == '고무오리 디버깅 끝':
        break
    if cycl == '문제':
        unsolved += 1
    elif cycl == '고무오리':
        if unsolved == 0:
            unsolved += 2
        elif unsolved >= 1:
            unsolved -= 1

if unsolved == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')