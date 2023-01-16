n = int(input())
nList = list(map(int, input().split()))
nList.sort()

print(nList[0] * nList[-1])