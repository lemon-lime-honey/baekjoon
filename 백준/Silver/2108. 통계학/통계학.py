import sys
from collections import Counter

n = int(input())
num = list()

for i in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

countNum = Counter(num).most_common()

print(round(sum(num)/n))
print(num[n//2])

if len(countNum) > 1:
    if countNum[0][1] == countNum[1][1]:
        print(countNum[1][0])
    else:
        print(countNum[0][0])
else:
    print(countNum[0][0])

print(num[n-1]-num[0])
