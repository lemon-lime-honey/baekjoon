import sys, re
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for i in range(n)]

words.sort(key=lambda x: len(x))
result = n

for i in range(n):
    flag = False
    for j in range(i + 1, n):
        if re.match(words[i], words[j]):
            flag = True
            break
    if flag: result -= 1

print(result)