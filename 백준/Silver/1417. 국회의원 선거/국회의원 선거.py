import heapq

n = int(input())
one = int(input())

if n == 1:
    print(0)
else:
    vote = list()
    result = 0

    for i in range(n - 1):
        heapq.heappush(vote, -1 * int(input()))
    
    while True:
        temp = heapq.heappop(vote)
        if (-1 * temp) < (one + result):
            break
        result += 1
        temp += 1
        heapq.heappush(vote, temp)
    
    print(result)