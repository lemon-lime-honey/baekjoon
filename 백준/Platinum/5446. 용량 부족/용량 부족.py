import sys

input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.last = False


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


def compare(e_node: TrieNode, l_node: TrieNode):
    global cnt

    if e_node.last:
        cnt += 1

    for letter in e_node.children.keys():
        if letter not in l_node.children:
            cnt += 1
            continue
        compare(e_node.children[letter], l_node.children[letter])


if __name__ == "__main__":
    n = int(input())
    result = list()

    for i in range(n):
        erase = Trie()
        left = Trie()
        cnt = 0

        n1 = int(input())

        for j in range(n1):
            erase.insert(input().rstrip())

        n2 = int(input())

        for j in range(n2):
            left.insert(input().rstrip())

        if n2 == 0:
            cnt = 1
        else:
            compare(erase.root, left.root)

        result.append(cnt)

    print(*result, sep="\n")
