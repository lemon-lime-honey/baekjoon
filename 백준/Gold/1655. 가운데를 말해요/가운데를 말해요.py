import heapq, sys
input = sys.stdin.readline

n = int(input())
first = list()
second = list()
result = list()

for i in range(n):
    ipt = int(input())
    if len(first) == len(second):
        heapq.heappush(first, (-1 * ipt, ipt))
    else:
        heapq.heappush(second, (ipt, ipt))

    if second and first[0][1] > second[0][1]:
        temp1 = heapq.heappop(first)[1]
        temp2 = heapq.heappop(second)[1]
        heapq.heappush(first, (-1 * temp2, temp2))
        heapq.heappush(second, (temp1, temp1))
    
    result.append(first[0][1])

print(*result, sep='\n')