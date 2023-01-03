x = list()
y = list()

for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

chkX = list()
chkY = list()

for i in x:
    if not (i in chkX):
        chkX.append(i)
    else:
        dupX = i

for i in y:
    if not (i in chkY):
        chkY.append(i)
    else:
        dupY = i

for i in range(3):
    if x[i] != dupX:
        x4 = x[i]
    if y[i] != dupY:
        y4 = y[i]

print('{0} {1}'.format(x4, y4))
