from sys import stdin

while True:
    input_content = stdin.readline().strip()

    if input_content == "# 0 0":
        break

    input_splitted = input_content.split()

    member_name = input_splitted[0]
    member_age, member_weight = map(int, input_splitted[1:])

    if member_age > 17 or member_weight >= 80:
        member_category = "Senior"
    else:
        member_category = "Junior"

    print(member_name, member_category)