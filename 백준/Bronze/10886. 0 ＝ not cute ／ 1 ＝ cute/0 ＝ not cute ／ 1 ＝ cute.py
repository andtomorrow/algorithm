N = int(input()) # N은 홀수

yes_cute = 0
not_cute = 0

for t in range(N):
    vote = int(input())
    if vote == 1:
        yes_cute += 1
    else:
        not_cute += 1

if yes_cute > not_cute:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')