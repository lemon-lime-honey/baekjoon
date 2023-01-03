from collections import deque

num = int(input())
card = deque([x for x in range(1, num + 1)])

while len(card) > 1:
    card.popleft()
    card.append(card[0])
    card.popleft()
print(card[0])