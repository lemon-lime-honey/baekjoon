import heapq


def backtrack(bracket_idx, route):
    if bracket_idx == k:
        number = 0
        for num in route:
            number = number * 10 + num
        heapq.heappush(small, number)
        heapq.heappush(big, -number)
        return

    for i in range(10):
        if (i not in nums and 
            (not route or
            (bracket[bracket_idx] == '<' and route[-1] < i) or
            (bracket[bracket_idx] == '>' and route[-1] > i))):
            nums.add(i)
            route.append(i)
            backtrack(bracket_idx + 1, route)
            route.pop()
            nums.discard(i)


k = int(input())
bracket = input().split()
small = list()
big = list()
nums = set()

backtrack(-1, list())

print(str(-1 * big[0]).zfill(k + 1), str(small[0]).zfill(k + 1), sep='\n')