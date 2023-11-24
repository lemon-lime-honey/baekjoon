from collections import defaultdict, deque


def solution(begin, target, words):
    if target not in words:
        return 0

    wordDict = defaultdict(list)
    words.append(begin)

    for word in words:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            wordDict[pattern].append(word)

    visited = set([begin])
    que = deque([begin])
    result = 0

    while que:
        n = len(que)
        for i in range(n):
            word = que.popleft()
            if word == target:
                return result
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                for next_word in wordDict[pattern]:
                    if next_word in visited:
                        continue
                    visited.add(next_word)
                    que.append(next_word)
        result += 1

    return 0