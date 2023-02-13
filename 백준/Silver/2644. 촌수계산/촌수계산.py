def dfs(target):
    stack = [target]
    result = list()

    while stack:
        now = stack.pop()
        result.append(now)
        for person in family_tree[now]:
            stack.append(person)
    
    return result

n = int(input())
family_tree = [[] for i in range(n + 1)]
t1, t2 = map(int, input().split())
cnt1, cnt2 = 0, 0
m = int(input())

for i in range(m):
    x, y = map(int, input().split())
    family_tree[y].append(x)

cnt1 = dfs(t1)
cnt2 = dfs(t2)

if cnt1[-1] == cnt2[-1]:
    try:
        while (cnt1[-1] == cnt2[-1]):
            cnt1.pop()
            cnt2.pop()
    except:
        pass
    print(len(cnt1) + len(cnt2))
else:
    print(-1)