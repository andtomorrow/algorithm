from collections import Counter

word = input()
ltr_cnt = Counter(word.upper())

if len(ltr_cnt.most_common()) == 1:
    print(ltr_cnt.most_common()[0][0])
elif ltr_cnt.most_common(2)[0][1] == ltr_cnt.most_common(2)[1][1]:
    print('?')
else:
    print(ltr_cnt.most_common()[0][0])