n = int(input())

series = ["ABC", "BABC", "CCAABB"]
nicknames = ["Adrian", "Bruno", "Goran"]
score = [0, 0, 0]
idx = [0, 0, 0]

answer = input()

for a in answer:
    if a == series[0][idx[0]]:
        score[0] += 1
    if a == series[1][idx[1]]:
        score[1] += 1
    if a == series[2][idx[2]]:
        score[2] += 1

    idx[0] = (idx[0] + 1) % 3
    idx[1] = (idx[1] + 1) % 4
    idx[2] = (idx[2] + 1) % 6

result = sorted(zip(nicknames, score), key=lambda x: -x[1])

print(result[0][1])
idx = 0

while idx < 3 and result[0][1] == result[idx][1]:
    print(result[idx][0])
    idx += 1
