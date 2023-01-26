money = ['Q', 'D', 'N', 'P']
money_cnt = [0, 0, 0, 0]
unit = [25, 10, 5, 1]

T = int(input())
for t in range(1, T+1):
    amount = int(input())
    for i in range(4):
        money_cnt[i], amount = divmod(amount, unit[i])
    print(*money_cnt)