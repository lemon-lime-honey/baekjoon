import sys
input = sys.stdin.readline


class Node:
    def __init__(self, val=0):
        self.val = val
        self.children = dict()
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()


    def insert(self, word):
        node = self.root

        for letter in word:
            chk = ord(letter)
            if chk not in node.children:
                new = Node(chk)
                node.children[chk] = new
            node = node.children[chk]

        node.end = True


    def search(self, row, col, head):
        def dfs(r, c, node, route):
            nonlocal result, visited

            if node.end:
                result.add(route)
                if not node.children: return

            for nr, nc in (
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
                (r - 1, c - 1),
                (r - 1, c + 1),
                (r + 1, c - 1),
                (r + 1, c + 1)
            ):
                if 0 <= nr < 4 and 0 <= nc < 4:
                    if (not visited[nr][nc] and
                        ord(board[nr][nc]) in node.children):
                        visited[nr][nc] = True
                        dfs(nr,
                            nc,
                            node.children[ord(board[nr][nc])],
                            route + board[nr][nc])
                        visited[nr][nc] = False


        result = set()
        visited = [[False for i in range(4)] for j in range(4)]
        visited[row][col] = True
        dfs(row, col, head, board[row][col])
        return result


trie = Trie()
score_dict = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11}

w = int(input())
for i in range(w):
    trie.insert(input().rstrip())

input()

b = int(input())
for i in range(b):
    board = [input().rstrip() for i in range(4)]

    found = set()

    for j in range(4):
        for k in range(4):
            if ord(board[j][k]) in trie.root.children:
                found.update(trie.search(
                    j, k,
                    trie.root.children[ord(board[j][k])]))

    answer = sorted(found, key=lambda x: (-len(x), x))
    score = 0

    for word in answer:
        score += score_dict[len(word)]

    print(score, answer[0], len(answer))

    if i != b - 1: input()