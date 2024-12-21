from collections import deque


def main(a, b, c):
    if (a + b + c) % 3:
        return False

    chk[a][b] = True
    total = a + b + c
    que = deque([(a, b)])

    while que:
        i, j = que.popleft()

        k = total - i - j

        if i == j == k:
            return True

        for u, v in (i, j), (j, k), (k, i):
            if u < v:
                nv = v - u
                nu = u + u
            elif u > v:
                nu = u - v
                nv = v + v
            else:
                continue

            if chk[nu][nv]:
                continue

            chk[nu][nv] = True
            que.append((nu, nv))

    return False


a, b, c = map(int, input().split())
chk = [[False for i in range(1501)] for j in range(1501)]
print(main(a, b, c) * 1)
