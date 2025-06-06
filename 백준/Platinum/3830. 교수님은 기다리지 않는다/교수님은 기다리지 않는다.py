import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find(p):
    if p == parent[p]:
        weight[p] = 0
        return p
    q = find(parent[p])
    weight[p] += weight[parent[p]]
    parent[p] = q
    return q


def union(p, q, w):
    np, nq = find(p), find(q)
    if np == nq:
        return False
    weight[nq] = -weight[q] + weight[p] + w
    parent[nq] = np
    return True


if __name__ == "__main__":
    result = list()

    while True:
        n, m = map(int, input().split())
        if n == m == 0:
            break
        parent = [i for i in range(n + 1)]
        weight = [0 for i in range(n + 1)]

        for i in range(m):
            ipt = input().split()
            if ipt[0] == '!':
                union(int(ipt[1]), int(ipt[2]), int(ipt[3]))
            elif ipt[0] == '?':
                a, b = int(ipt[1]), int(ipt[2])
                na, nb = find(a), find(b)
                if na != nb:
                    result.append("UNKNOWN")
                else:
                    result.append(weight[b] - weight[a])

    print(*result, sep="\n")
