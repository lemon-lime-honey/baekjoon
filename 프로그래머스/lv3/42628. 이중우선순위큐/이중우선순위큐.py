import heapq

def solution(operations):
    maxheap = list()
    minheap = list()
    chkset = set()
    result = [0, 0]

    for index, operation in enumerate(operations):
        op, num = operation.split(' ')
        if op == 'I':
            heapq.heappush(maxheap, (-1 * int(num), index))
            heapq.heappush(minheap, (int(num), index))
            chkset.add(index)
        elif num == '1':
            while maxheap:
                temp = heapq.heappop(maxheap)
                if temp[1] in chkset:
                    chkset.remove(temp[1])
                    break
        else:
            while minheap:
                temp = heapq.heappop(minheap)
                if temp[1] in chkset:
                    chkset.remove(temp[1])
                    break

    while maxheap:
        temp = heapq.heappop(maxheap)
        if temp[1] in chkset:
            result[0] = -1 * temp[0]
            chkset.remove(temp[1])
            break

    while minheap:
        temp = heapq.heappop(minheap)
        if temp[1] in chkset:
            result[1] = temp[0]
            chkset.remove(temp[1])
            break

    return result