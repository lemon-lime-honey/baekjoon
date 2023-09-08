import sys
input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.value = None


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, number):
        chk = self.root
        flag = True

        for i in range(len(number)):
            if number[i] in chk.children:
                chk = chk.children[number[i]]
                if hasattr(chk, 'last'): flag = False
                if i == len(number) - 1: flag = False
            else:
                new = TrieNode()
                new.value = number[i]
                chk.children[number[i]] = new
                chk = chk.children[number[i]]
            if i == len(number) - 1:
                chk.last = True

        return flag


t = int(input())

for i in range(t):
    n = int(input())
    trie = Trie()
    result = True

    for j in range(n):
        number = input().rstrip()
        flag = trie.insert(number)
        if not flag: result = False

    print('YES' if result else 'NO')