from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input()) 
cards = list(map(int, input().split()))
result = [cards[0]]

for i in range(1, n):
    if result[-1] < cards[i]:
        result.append(cards[i])
    else:
        idx = bisect_left(result, cards[i])
        result[idx] = cards[i]

print(len(result))