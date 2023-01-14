import sys
from collections import Counter

def find(search_list, value):
    low = 0
    mid = 0
    high = len(search_list) - 1
    while(low <= high):
        mid = (low + high) // 2
        if value == search_list[mid][0]:
            return search_list[mid][1]
        elif search_list[mid][0] > value:
            high = mid - 1
        elif search_list[mid][0] < value:
            low = mid + 1
    return 0

n = int(sys.stdin.readline())
nList = Counter(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split()))
nList = sorted(nList.items())
result = list()

for item in mList:
    result.append(str(find(nList, item)))
print(' '.join(result))