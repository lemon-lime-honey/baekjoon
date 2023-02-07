import heapq

def solution(numlist, n):
    answer = list()
    heap = list()

    for number in numlist:
        heapq.heappush(heap, (abs(number - n), -1 *  number))
    
    for i in range(len(heap)):
        answer.append(-1 * heapq.heappop(heap)[1])
    
    return answer