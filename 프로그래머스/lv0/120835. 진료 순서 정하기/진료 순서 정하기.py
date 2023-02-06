import heapq

def solution(emergency):
    heap = list()
    answer = [0] * len(emergency)
    
    for index, value in enumerate(emergency):
        heapq.heappush(heap, (-1 * value, index))
    
    for i in range(len(emergency)):
        answer[heapq.heappop(heap)[1]] = i + 1
    
    return answer