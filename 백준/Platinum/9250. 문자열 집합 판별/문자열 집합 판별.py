from collections import deque
import sys

input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.failure = None
        self.last = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, target):
        node = self.root

        for c in target:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.last = True

    def set_failure(self):
        node = self.root
        que = deque()

        for child in node.children.values():
            child.failure = node
            que.append(child)

        while que:
            now = que.popleft()
            for c, child in now.children.items():
                fail_node = now.failure
                while fail_node != self.root and c not in fail_node.children:
                    fail_node = fail_node.failure
                if c in fail_node.children:
                    child.failure = fail_node.children[c]
                else:
                    child.failure = self.root
                que.append(child)

    def find(self, target):
        node = self.root

        for c in target:
            while node != self.root and c not in node.children:
                node = node.failure

            if c in node.children:
                node = node.children[c]

            temp = node
            while temp != self.root:
                if temp.last:
                    return True
                temp = temp.failure

        return False


trie = Trie()

n = int(input())

for i in range(n):
    trie.insert(input().rstrip())

trie.set_failure()

q = int(input())

for i in range(q):
    if trie.find(input().rstrip()):
        print("YES")
    else:
        print("NO")
