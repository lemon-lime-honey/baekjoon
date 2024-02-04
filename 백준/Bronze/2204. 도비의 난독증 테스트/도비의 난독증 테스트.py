import heapq

while True:
    n = int(input())

    if n == 0:
        break

    words = list()

    for i in range(n):
        word = input()
        heapq.heappush(words, (word.lower(), word))

    print(words[0][1])