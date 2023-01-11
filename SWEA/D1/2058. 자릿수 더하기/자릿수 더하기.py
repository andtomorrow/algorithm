usr_input = input()

lngth = len(usr_input)
usr_num = int(usr_input)
sum_all_nums = 0
for i in range(lngth):
    sum_all_nums += usr_num % 10
    usr_num //= 10
print(sum_all_nums)