from collections import Counter

t = int(input())

for i in range(t):
    counter = Counter(input().replace(' ', ''))
    result = counter.most_common()
    if len(result) > 1 and result[0][1] == result[1][1]:
        print('?')
    else:
        print(result[0][0])