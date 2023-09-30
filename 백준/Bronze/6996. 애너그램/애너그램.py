import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    aLetter = [0 for j in range(26)]
    bLetter = [0 for j in range(26)]
    a, b = input().rstrip().split()

    for letter in a:
        aLetter[ord(letter) - ord('a')] += 1

    for letter in b:
        bLetter[ord(letter) - ord('a')] += 1

    print(a, '&', b, 'are', end=' ')
    print('NOT ' if aLetter != bLetter else '', end='')
    print('anagrams.')