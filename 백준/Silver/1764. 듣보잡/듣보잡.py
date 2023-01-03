import sys

def search(search_list, value):
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

n, m = map(int, sys.stdin.readline().split())
name = []
count = 0
found = []

for i in range(n):
    name.append(sys.stdin.readline().strip())

name.sort()

for j in range(m):
    temp = sys.stdin.readline().strip()
    if search(name, temp):
        count += 1
        found.append(temp)

found.sort()
print(count)
for item in found:
    print(item)