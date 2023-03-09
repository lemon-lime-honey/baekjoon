stroke = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

a = input()
b = input()
score = list()

for i in range(len(a)):
    score.append(stroke[ord(a[i]) - 65])
    score.append(stroke[ord(b[i]) - 65])

ref = 0
temp = list()

while True:
    if ref < (len(score) - 1):
        now = score[ref] + score[ref + 1]
        if now >= 10:
            now %= 10
        temp.append(now)
        ref += 1
    else:
        ref = 0
        score = temp
        temp = list()
        if len(score) == 2:
            print(*score, sep='')
            break