from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    change_total = int(stdin.readline())
    n_of_quarter, after_quarter = divmod(change_total, 25)
    n_of_dime, after_dime = divmod(after_quarter, 10)
    n_of_nickel, after_nickel = divmod(after_dime, 5)
    n_of_penny = after_nickel

    print(n_of_quarter, n_of_dime, n_of_nickel, n_of_penny, sep=" ")
