def censor_word(word):
    result_word = ''
    for char in word:
        if char not in prohibited_chars:
            result_word += char
        else:
            pass
    return result_word

prohibited_chars = []
for char in 'CAMBRIDGE':
    prohibited_chars.append(char)

print(censor_word(input()))