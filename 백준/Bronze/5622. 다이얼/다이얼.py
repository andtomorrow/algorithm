chars = {
    2:'ABC',
    3:'DEF',
    4:'GHI',
    5:'JKL',
    6:'MNO',
    7:'PQRS',
    8:'TUV',
    9:'WXYZ'
}

dialing = 0

def dial(string):
    for i in range(len(string)):
        for k, v in chars.items():
            if string[i] in v:
                global dialing
                dialing += k + 1

dial_string = input()
dial(dial_string)

print(dialing)