n = int(input())
s = input()

cnt = 1
result = 0

for i in range(1, n):
    if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i]) - ord(s[i - 1]) == -1:
        cnt += 1
    else:
        cnt = 1
    result = max(result, cnt)

print("YES" if result >= 5 else "NO")
