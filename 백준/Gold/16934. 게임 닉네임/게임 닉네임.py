import sys
input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.name = dict()

 
    def insert(self, nickname):
        if nickname in self.name:
            self.name[nickname] += 1
            return f'{nickname}{self.name[nickname]}'

        self.name[nickname] = 1
        node = self.root
        flag = False
        res = ''

        for letter in nickname:
            target = ord(letter) - ord('a')
            if not flag:
                res += letter
            if node.children[target] is None:
                node.children[target] = TrieNode()
                flag = True
            node = node.children[target]

        return res



n = int(input())
trie = Trie()

for i in range(n):
    print(trie.insert(input().rstrip()))