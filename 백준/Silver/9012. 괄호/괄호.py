T = int(input())

for t in range(1, T+1):
    ln = input()
    open_parenthese = 0
    for char in ln:
        if char == '(':
            open_parenthese += 1
        elif char == ')':
            open_parenthese -= 1

        if open_parenthese < 0:
            validity = 'NO'
            break
    
    if open_parenthese == 0:
        validity = 'YES'
    else:
        validity = 'NO'
    print(validity)