import sys
input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.val = None
        self.children = dict()
        self.depth = -1


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, words):
        node = self.root

        for word in words:
            if word not in node.children:
                new = TrieNode()
                new.val = word
                node.children[word] = new
                node.children[word].depth = node.depth + 1

            node = node.children[word]


def show(node):
    print(' ' * node.depth + node.val)

    for child in sorted(node.children.keys()):
        show(node.children[child])


n = int(input())
trie = Trie()

for i in range(n):
    ipt = input().rstrip().split('\\')
    trie.insert(ipt)

for child in sorted(trie.root.children.keys()):
    show(trie.root.children[child])