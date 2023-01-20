un, deux, trois, quatre, cinq = input().split()
nombres = [un, deux, trois, quatre, cinq] # memb: STR

values_nombres = [int(n) for n in nombres]
in_order = sorted(values_nombres)

stage = nombres
while stage != list(map(str, in_order)):
    for i in range(4):
        if int(stage[i]) > int(stage[i+1]):
            stage[i], stage[i+1] = stage[i+1], stage[i]
            print(*nombres)
