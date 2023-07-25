import heapq

def solution(rank, attendance):
    result = list()
    final = list()
    for i in range(len(rank)):
        if attendance[i]:
            heapq.heappush(result, (rank[i], i))
    for i in range(3):
        student = heapq.heappop(result)
        final.append(student[1])
    return 10000 * final[0] + 100 * final[1] + final[2]