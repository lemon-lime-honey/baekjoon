n = int(input())
cards = list(map(int, input().split()))
chk = [False for i in range(1000001)]
score = [0 for i in range(1000001)]

for card in cards:
    chk[card] = True

for card in cards:
    for i in range(card * 2, 1000001, card):
        if chk[i]:
            score[card] += 1
            score[i] -= 1

for card in cards:
    print(score[card], end=' ')