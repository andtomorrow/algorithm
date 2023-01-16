d1, d2, d3 = map(int, input().split())

dices = [d1, d2, d3]

dice_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for num in dices:
    dice_dict[num] += 1

if max(dice_dict.values()) == 3:
    for k, v in dice_dict.items():
        if v == 3:
            reward = 10000 + k * 1000
            break

elif max(dice_dict.values()) == 2:
    for k, v in dice_dict.items():
        if v == 2:
            reward = 1000 + k * 100
            break

elif max(dice_dict.values()) == 1:
    reward = max(dices) * 100

print(reward)