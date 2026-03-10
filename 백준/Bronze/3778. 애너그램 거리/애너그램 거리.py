n = int(input())

for i in range(n):
    cnt = [0 for i in range(26)]
    first = input()

    for letter in first:
        cnt[ord(letter) - ord("a")] += 1

    second = input()

    for letter in second:
        cnt[ord(letter) - ord("a")] -= 1

    result = 0

    for c in cnt:
        result += abs(c)

    print(f"Case #{i + 1}: {result}")
