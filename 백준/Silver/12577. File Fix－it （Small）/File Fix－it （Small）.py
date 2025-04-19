class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path):
        route = path[1:].split("/")
        node = self.root
        result = 0

        for directory in route:
            if directory not in node.children:
                node.children[directory] = TrieNode()
                result += 1
            node = node.children[directory]
        node.last = True
        
        return result


class TrieNode:
    def __init__(self, last=False):
        self.children = dict()
        self.last = last


t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    trie = Trie()
    result = 0

    for j in range(n):
        trie.insert(input())
        
    for j in range(m):
        result += trie.insert(input())
        
    print(f"Case #{i + 1}: {result}")
