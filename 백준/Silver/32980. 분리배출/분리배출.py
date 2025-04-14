from collections import Counter

n = int(input())
trash = [input() for i in range(n)]

p, c, v, s, g, f = map(int, input().split())
o = int(input())

result = 0

for t in trash:
    cnt = Counter(t).most_common()
    if len(cnt) == 1:
        if cnt[0][0] == "O":
            result += o * len(t)
        else:
            match cnt[0][0]:
                case "P":
                    result += min(p, o) * len(t)
                case "C":
                    result += min(c, o) * len(t)
                case "V":
                    result += min(v, o) * len(t)
                case "S":
                    result += min(s, o) * len(t)
                case "G":
                    result += min(g, o) * len(t)
                case "F":
                    result += min(f, o) * len(t)
    else:
        result += o * len(t)

print(result)
