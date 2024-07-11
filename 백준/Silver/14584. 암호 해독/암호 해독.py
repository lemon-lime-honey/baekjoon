import re


def solve():
    for i in range(26):
        temp = list()
        for letter in quiz:
            temp.append(chr((ord(letter) - ord('a') + i) % 26 + ord('a')))

        chk = ''.join(temp)

        for word in words:
            if re.search(word, chk): return chk


quiz = input()
n = int(input())
words = [input() for i in range(n)]
print(solve())
