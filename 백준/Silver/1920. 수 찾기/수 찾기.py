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
numLst = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
numLst.sort()

for item in target:
    print(find(numLst, item))