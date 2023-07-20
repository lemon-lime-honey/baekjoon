from collections import Counter
from sys import exit

name = input()
letter_cnt = Counter(name)
letter = list()
center = ''
odd = 0

for key, value in letter_cnt.items():
    if value % 2:
        if odd:
            print('I\'m Sorry Hansoo')
            exit()
        odd += 1
        center = key
        if value > 1:
            for i in range((value - 1) // 2):
                letter.append(key)
    else:
        for i in range(value // 2):
            letter.append(key)

letter.sort()

print(''.join(letter) + center + ''.join(letter[::-1]))