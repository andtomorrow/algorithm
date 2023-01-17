def validate_num(num_lst):
    five_digits = [*num_lst]
    somme = 0
    for i in range(5):
        somme += five_digits[i] ** 2
    return somme % 10

num_lst = list(map(int, input().split()))
print(validate_num(num_lst))