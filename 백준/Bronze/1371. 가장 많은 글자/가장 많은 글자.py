from collections import defaultdict

cnt = defaultdict(int)

while True:
    try:
        ipt = input()
        for letter in ipt:
            if letter == ' ': continue
            cnt[letter] += 1
    except:
        break

result = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
target = result[0][1]

for letter, num in result:
    if num != target: break
    print(letter, end='')