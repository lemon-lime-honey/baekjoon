string = list()
max = 0
for i in range(5):
    temp = input()
    string.append(temp)
    if max < len(temp):
        max = len(temp)

for i in range(max):
    for j in range(5):
        try:
            print(string[j][i], end = '')
        except:
            continue