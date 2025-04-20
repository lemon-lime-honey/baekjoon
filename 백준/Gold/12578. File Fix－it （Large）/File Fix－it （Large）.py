import sys

input = sys.stdin.readline


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path):
        directories = path[1:].split("/")
        node = self.root
        result = 0
        
        for directory in directories:
            if directory not in node.children:
                node.children[directory] = TrieNode()
                result += 1
            node = node.children[directory]
        node.last = True

        return result


class TrieNode:
    def __init__(self):
        self.children = dict()

t = int(input())

for i in range(t):
    trie = Trie()

    n, m = map(int, input().split())
    result = 0

    for j in range(n):
        trie.insert(input().rstrip())

    for j in range(m):
        result += trie.insert(input().rstrip())

    print(f"Case #{i + 1}: {result}")
