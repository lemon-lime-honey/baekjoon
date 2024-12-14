from copy import deepcopy
import sys

input = sys.stdin.readline

r, c = map(int, input().split())

card = [list(input().rstrip()) for i in range(r)]

for i in range(r):
    card[i].extend(card[i][::-1])

for i in range(r - 1, -1, -1):
    card.append(deepcopy(card[i]))

a, b = map(int, input().split())

if card[a - 1][b - 1] == "#":
    card[a - 1][b - 1] = "."
else:
    card[a - 1][b - 1] = "#"

for line in card:
    print("".join(line))
