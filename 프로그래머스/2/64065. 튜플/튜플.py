import heapq

def solution(s: str):
    result = list()
    tuples = list()
    data = s[:-2].replace('{', '').split('}')

    for tup in data:
        ipt = tup.split(',')
        temp = list()
        for num in ipt:
            if num.isdigit():
                temp.append(int(num))
        heapq.heappush(tuples, (len(temp), temp))

    while tuples:
        nums = heapq.heappop(tuples)[1]
        for num in nums:
            if num not in result:
                result.append(num)
                break

    return result