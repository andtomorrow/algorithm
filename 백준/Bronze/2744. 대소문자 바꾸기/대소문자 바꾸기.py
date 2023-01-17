word = input()
rvsd_word = ''
for char in word:
    if str.islower(char):
        rvsd_word += char.upper()
    elif str.isupper(char):
        rvsd_word += char.lower()

print(rvsd_word)