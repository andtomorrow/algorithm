while True:
    inp_ = input()
    if inp_ == '0':
        break

    for i in range(len(inp_)):
        if inp_[i] != inp_[-i-1]:
            result = 'no'
            break
        result = 'yes'
    
    print(result)    