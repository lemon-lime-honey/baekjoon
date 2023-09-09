import sys
input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.value = None


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, string):
        chk = self.root

        for i in range(len(string)):
            if string[i] in chk.children:
                chk = chk.children[string[i]]
            else:
                new = TrieNode()
                new.value = string[i]
                chk.children[string[i]] = new
                chk = chk.children[string[i]]
            if i == len(string) - 1:
                chk.last = True


    def prefix(self, string):
        chk = self.root

        for i in range(len(string)):
            if string[i] in chk.children:
                chk = chk.children[string[i]]
            else: return False

        return True


n, m = map(int, input().split())
trie = Trie()
result = 0

for i in range(n):
    s = input().rstrip()
    trie.insert(s)

for i in range(m):
    s = input().rstrip()
    if trie.prefix(s): result += 1

print(result)