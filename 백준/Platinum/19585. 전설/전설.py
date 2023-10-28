import sys
input = sys.stdin.readline


class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode(None)


    def insert(self, string):
        node = self.root

        for i in range(len(string)):
            chk = ord(string[i]) - 97
            if chk not in node.children:
                new = TrieNode(chk)
                node.children[chk] = new
            node = node.children[chk]

        node.end = True


    def search(self, string):
        node = self.root

        for i in range(len(string)):
            chk = ord(string[i]) - 97
            if node.end and string[i:] in name: return True
            if chk in node.children:
                node = node.children[chk]
            else: return False


c, n = map(int, input().split())
color = Trie()
name = set()

for i in range(c):
    color.insert(input().rstrip())

for i in range(n):
    name.add(input().rstrip())

q = int(input())

for i in range(q):
    target = input().rstrip()
    print('Yes' if color.search(target) else 'No')