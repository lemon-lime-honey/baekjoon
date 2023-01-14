import sys

def find(search_list, value):
    low = 0
    mid = 0
    high = len(search_list) - 1
    while(low <= high):
        mid = (low + high) // 2
        if value == search_list[mid]:
            return 1
        elif search_list[mid] > value:
            high = mid - 1
        elif search_list[mid] < value:
            low = mid + 1
    return 0

n = int(sys.stdin.readline())
nList = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split()))
nList.sort()
result = list()

for item in mList:
    result.append(str(find(nList, item)))
print(' '.join(result))