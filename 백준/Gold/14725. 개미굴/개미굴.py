import sys
input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.last = False
        self.val = None
        self.depth = -1


class Trie:
    def __init__(self):
        self.root = TrieNode()


def search(node):
    print('--' * node.depth + node.val)

    if node.last: return

    for child in sorted(node.children.keys()):
        search(node.children[child])


n = int(input())
result = list()
trie = Trie()

for i in range(n):
    ipt = input().rstrip().split()
    node = trie.root

    for j in range(1, len(ipt)):
        if ipt[j] not in node.children:
            node.children[ipt[j]] = TrieNode()
            node.children[ipt[j]].val = ipt[j]
            node.children[ipt[j]].depth = node.depth + 1
        node = node.children[ipt[j]]

    node.last = True

for child in sorted(trie.root.children.keys()):
    search(trie.root.children[child])