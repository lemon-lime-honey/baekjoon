import heapq

word = input()
length = len(word)
words = list()

for i in range(length - 2):
    for j in range(i + 1, length - 1):
        heapq.heappush(words, word[i::-1] + word[j:i:-1] + word[:j:-1])

print(words[0])