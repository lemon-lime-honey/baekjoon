import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))


def get_preorder(ii, ie, pi, pe):
    if ii > ie or pi > pe: return

    root = postorder[pe]
    print(root, end=' ')

    one = pos[root] - ii
    two = ie - pos[root]

    get_preorder(ii, ii + one - 1, pi, pi + one - 1)
    get_preorder(ie - two + 1, ie, pe - two, pe - 1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = [0 for i in range(n + 1)]

for i in range(n):
    pos[inorder[i]] = i

get_preorder(0, n - 1, 0, n - 1)