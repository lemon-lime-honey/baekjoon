n = int(input())
alpha = input()

cnt = [0 for i in range(26)]
result = 1001

for letter in alpha:
    cnt[ord(letter) - ord("A")] += 1

for letter in "BRONZESILVER":
    if letter in "ER":
        result = min(result, cnt[ord(letter) - ord("A")] // 2)
    else:
        result = min(result, cnt[ord(letter) - ord("A")])

print(result)
