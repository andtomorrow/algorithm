voyelles = 'aeiou'

while True:
    case_in = input()
    if case_in == '#':
        break
    else:
        num_voyelles = 0
        for i in range(5):
            num_voyelles += case_in.lower().count(voyelles[i])
        print(num_voyelles)