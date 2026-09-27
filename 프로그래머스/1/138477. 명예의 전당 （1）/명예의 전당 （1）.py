import heapq

def solution(k, score):
    answer = list()
    hq = list()
    
    for s in score:
        heapq.heappush(hq, s)
        if len(hq) > k:
            heapq.heappop(hq)
        answer.append(hq[0])
    
    return answer