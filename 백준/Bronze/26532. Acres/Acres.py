from math import ceil

side = list(map(int, input().split()))
print(ceil(side[0] * side[1] / 4840 / 5))