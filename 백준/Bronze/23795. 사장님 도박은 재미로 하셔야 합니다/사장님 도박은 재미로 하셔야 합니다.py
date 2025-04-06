from sys import stdin

money_spent = 0

while True:
    input_num = int(stdin.readline())

    if input_num == -1:
        break

    money_spent += input_num

print(money_spent)
