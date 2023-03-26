import sys
input = sys.stdin.readline

def backtrack(start: int):
    global consonant, vowel
    if len(answer) == l:
        if consonant > 1 and vowel > 0:
            print(*answer, sep='')
            return
    
    for i in range(start, c):
        answer.append(letters[i])
        if letters[i] in 'aeiou':
            vowel += 1
        else:
            consonant += 1
        backtrack(i + 1)
        answer.pop()
        if letters[i] in 'aeiou':
            vowel -= 1
        else:
            consonant -= 1

l, c = map(int, input().split())
letters = list(input().split())
answer = list()
letters.sort()
consonant = 0
vowel = 0

backtrack(0)