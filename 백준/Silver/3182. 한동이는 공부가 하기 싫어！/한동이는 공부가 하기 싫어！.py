n = int(input())
link = [0 for i in range(n + 1)]
longest = list()
track = list()

for i in range(1, n + 1):
    link[i] = int(input())

for i in range(1, n + 1):
    stack = [i]
    track = list()
    rel = list()

    for element in link:
        rel.append(element)

    while stack:
        now = stack.pop()
        track.append(now)
        if len(longest) < len(track):
            longest = track
        elif len(longest) == len(track) and track[0] < longest[0]:
            longest = track
        if rel[now]:
            stack.append(rel[now])
            rel[now] = 0
        else:
            break

print(longest[0])