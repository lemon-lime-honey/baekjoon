import sys
input = sys.stdin.readline


def find(p):
    if p != people[p]:
        people[p] = find(people[p])
    return people[p]


def union(p, q):
    p, q = find(p), find(q)
    if p in truth and q in truth:
        return
    elif p in truth:
        people[q] = p
    elif q in truth:
        people[p] = q
    else:
        people[max(p, q)] = min(p, q)


n, m = map(int, input().split())
people = [i for i in range(n + 1)]
truth = set(list(map(int, input().split()))[1:])
parties = list()
result = 0

for i in range(m):
    party = list(map(int, input().split()))
    parties.append(party[1:])

    for j in range(1, party[0]):
        union(party[j], party[j + 1])

for party in parties:
    for participant in party:
        chk = find(participant)
        if chk in truth: break
    else: result += 1

print(result)