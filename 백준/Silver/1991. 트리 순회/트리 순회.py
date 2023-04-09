def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[nodes[root]][0])
        preorder(tree[nodes[root]][1])


def inorder(root):
    if root != '.':
        inorder(tree[nodes[root]][0])
        print(root, end='')
        inorder(tree[nodes[root]][1])
        

def postorder(root):
    if root != '.':
        postorder(tree[nodes[root]][0])
        postorder(tree[nodes[root]][1])
        print(root, end='')


n = int(input())
tree = [[] for i in range(n)]
nodes = dict()

for i in range(n):
    parent, left, right = input().split()
    nodes[parent] = i
    tree[i].append(left)
    tree[i].append(right)

preorder('A')
print()
inorder('A')
print()
postorder('A')