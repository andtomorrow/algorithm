while True:
    case_input = input()
    if case_input == '0 0 0':
        break
    elif case_input:
        sides = []
        sides.extend(map(int, case_input.split()))
        sides.sort()
        longest = sides.pop()
        other_s1, other_s2 = sides
        if longest ** 2 == other_s1 ** 2 + other_s2 ** 2:
            print('right')
        else:
            print('wrong')