n = int(input())
lst = list(map(float, input().split()))

numMax = max(lst)
newSum = 0

for i in lst:
    newSum += i/numMax*100

newAvg = newSum/n

print(newAvg)
