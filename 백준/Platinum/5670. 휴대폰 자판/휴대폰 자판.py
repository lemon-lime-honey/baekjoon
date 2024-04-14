import sys
input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.children = dict()


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]

        node.last = True


    def search(self, word):
        node = self.root.children[word[0]]
        result = 1

        for i in range(1, len(word) + 1):
            if i == len(word):
                return result
            if len(node.children) > 1 or hasattr(node, 'last'):
                result += 1
            node = node.children[word[i]]


while True:
    try:
        n = int(input())
    except:
        break

    words = list()
    trie = Trie()

    for i in range(n):
        words.append(input().rstrip())
        trie.insert(words[-1])

    cnt = 0

    for word in words:
        cnt += trie.search(word)

    print(f'{cnt / n:.2f}')