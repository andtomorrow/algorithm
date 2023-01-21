s = input()
out_ltr_cnt = 0
three_ltr = ['dz=']
two_ltr = [
    'c=',
    'c-',
    'd-',
    'lj',
    'nj',
    's=',
    'z='
]
    
while len(s) > 0:
    if len(s) >= 3:
        if s[0:3] in three_ltr:
            s = s.replace(s[0:3], '', 1)
            out_ltr_cnt += 1
            continue

    if len(s) >= 2:
        if s[0:2] in two_ltr:
            s = s.replace(s[0:2], '', 1)
            out_ltr_cnt += 1
            continue
            
    if len(s) >= 1:
        s = s.replace(s[0], '', 1)
        out_ltr_cnt += 1
        continue

print(out_ltr_cnt)