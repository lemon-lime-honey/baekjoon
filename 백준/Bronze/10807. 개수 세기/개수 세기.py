n = int(input())
numList = list(map(int, input().split()))
numFind = int(input())
count = 0

for num in numList:
    if num == numFind:
        count += 1

print(count)