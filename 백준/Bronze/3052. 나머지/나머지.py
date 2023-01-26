quotients = []

for n in range(10):
    num = (int(input()))
    qtn = num % 42
    if qtn not in quotients:
        quotients.append(qtn)

print(len(quotients))