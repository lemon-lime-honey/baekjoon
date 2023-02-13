cardA = list(map(int, input().split()))
cardB = list(map(int, input().split()))
scoreA = 0
scoreB = 0
last = -1

for i in range(10):
    if cardA[i] > cardB[i]:
        scoreA += 3
        last = i
    elif cardA[i] < cardB[i]:
        scoreB += 3
        last = i
    else:
        scoreA += 1
        scoreB += 1

print(scoreA, scoreB)
if scoreA == scoreB:
    if last == -1:
        print('D')
    else:
        if cardA[last] > cardB[last]:
            print('A')
        else:
            print('B')
elif scoreA > scoreB:
    print('A')
else:
    print('B')