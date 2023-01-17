x_crd = []
y_crd = []

def listupXY(point):
    x_crd.append(point[0])
    y_crd.append(point[1])

P1 = list(map(int, input().split()))
listupXY(P1)

P2 = list(map(int, input().split()))
listupXY(P2)

P3 = list(map(int, input().split()))
listupXY(P3)

x_cnt = {}
for x in x_crd:
    if x not in x_cnt:
        x_cnt[x] = 1
    else:
        x_cnt[x] += 1

y_cnt = {}
for y in y_crd:
    if y not in y_cnt:
        y_cnt[y] = 1
    else:
        y_cnt[y] += 1

for k, v in x_cnt.items():
    if v == 1:
        the_x = k
        break

for k, v in y_cnt.items():
    if v == 1:
        the_y = k
        break

print(the_x, the_y)