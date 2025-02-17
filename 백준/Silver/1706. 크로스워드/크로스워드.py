import heapq

r, c = map(int, input().split())
puzzle = [input() for i in range(r)]

wordDict = list()

for i in range(r):
    words = puzzle[i].split("#")
    for word in words:
        if len(word) < 2:
            continue
        heapq.heappush(wordDict, word)

vertical = list(map(list, zip(*puzzle)))

for i in range(c):
    words = "".join(vertical[i]).split("#")
    for word in words:
        if len(word) < 2:
            continue
        heapq.heappush(wordDict, word)

print(wordDict[0])
