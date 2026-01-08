n = int(input())
size = list(map(int, input().split()))

box = [0 for i in range(5)]
for s in size:
    box[s] += 1

result = 0
result += box[4]

cnt = min(box[3], box[1])
result += box[3]
box[1] -= cnt

result += box[2] // 2
box[2] %= 2

if box[2]:
    result += 1
    box[1] = max(0, box[1] - 2)

result += (box[1] + 3) // 4

print(result)
