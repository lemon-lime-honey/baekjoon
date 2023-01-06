import sys

money = 0
max = 0
n = int(sys.stdin.readline())

for i in range(n):
    dice = list(map(int, sys.stdin.readline().split()))
    if (dice[0] == dice[1]) * (dice[1] == dice[2]):
        money = 10000 + dice[0] * 1000
    elif (dice[0] == dice[1]) + (dice[0] == dice[2]):
        money = 1000 + dice[0] * 100
    elif (dice[1] == dice[2]):
        money = 1000 + dice[1] * 100
    else:
        dice.sort()
        money = dice[2] * 100
    if max < money:
        max = money

print(max)