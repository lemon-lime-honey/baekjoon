from collections import Counter

t = int(input())

for i in range(t):
    x = input()
    print(len(Counter(x)))
