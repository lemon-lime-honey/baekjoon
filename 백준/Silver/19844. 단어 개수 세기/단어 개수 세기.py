import re

front = {'c', 'j', 'n', 'm', 't', 's', 'l', 'd', 'qu'}
vowels = 'aeiouh'
words = re.split(r' |-', input())
result = 0

for word in words:
    chk = word.split('\'')
    if (len(chk) == 1 or
        not (chk[0] in front and
             chk[1][0] in vowels)):
        result += 1
    else:
        result += 2

print(result)