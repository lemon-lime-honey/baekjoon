from collections import defaultdict

t = int(input())
result = list()

for i in range(t):
    ipt = input()
    letters = defaultdict(int)

    for letter in ipt:
        if letter.isalpha():
            letters[letter.lower()] += 1

    cnt = sorted(letters.values(), reverse=True)

    if len(cnt) == 26:
        if cnt[-1] >= 3:
            result.append(f"Case {i + 1}: Triple pangram!!!")
        elif cnt[-1] >= 2:
            result.append(f"Case {i + 1}: Double pangram!!")
        else:
            result.append(f"Case {i + 1}: Pangram!")
    else:
        result.append(f"Case {i + 1}: Not a pangram")

print(*result, sep="\n")
