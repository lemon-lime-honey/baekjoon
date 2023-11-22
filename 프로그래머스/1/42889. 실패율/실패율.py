import heapq

def solution(N, stages):
    stay = [0 for i in range(N + 1)]
    reach = [0 for i in range(N + 1)]
    answer = list()
    heap = list()

    for i in range(len(stages)):
        stay[stages[i] - 1] += 1
        for j in range(stages[i]):
            reach[j] += 1

    for i in range(N):
        if reach[i] != 0:
            heapq.heappush(heap, (-1 * stay[i] / reach[i], i + 1))
        else:
            heapq.heappush(heap, (0, i + 1))

    while heap:
        answer.append(heapq.heappop(heap)[1])

    return answer