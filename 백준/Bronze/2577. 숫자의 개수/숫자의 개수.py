import collections

A = int(input())
B = int(input())
C = int(input())

mlt_string = str(A * B * C)
nums_cnt = collections.Counter(mlt_string)


for n in range(10):
    if str(n) in nums_cnt:
        print(nums_cnt[str(n)])
    else:
        print(0)