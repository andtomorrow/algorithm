seung_inpt = input()

happy = ':-)'
sad = ':-('

try:
    happy_face = seung_inpt.count(happy)
except:
    happy_face = 0

try:
    sad_face = seung_inpt.count(sad)
except:
    sad_face = 0

if happy_face == sad_face == 0:
    seung_emotion = 'none'
else:
    if happy_face == sad_face:
        seung_emotion = 'unsure'
    elif happy_face > sad_face:
        seung_emotion = 'happy'
    else:
        seung_emotion = 'sad'

print(seung_emotion)