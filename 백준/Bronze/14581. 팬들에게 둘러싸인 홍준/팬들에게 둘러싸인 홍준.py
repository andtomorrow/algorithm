from sys import stdin

input_hongjun = stdin.readline().strip()

emoticon_hongjun = ":"+input_hongjun+":"
emoticon_fan = ":fan:"

print(emoticon_fan*3, emoticon_fan+emoticon_hongjun +
      emoticon_fan, emoticon_fan*3, sep="\n")
