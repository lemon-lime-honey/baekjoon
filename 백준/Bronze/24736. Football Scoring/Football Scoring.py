score = [6, 3, 2, 1, 2]

vTeam = list(map(int, input().split()))
hTeam = list(map(int, input().split()))
vScore = 0
hScore = 0

for i in range(5):
    vScore += score[i] * vTeam[i]
    hScore += score[i] * hTeam[i]

print(f'{vScore} {hScore}')