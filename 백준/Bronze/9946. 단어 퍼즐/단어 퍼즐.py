import sys

input = sys.stdin.readline

index = 1

while True:
    word1 = input().rstrip()
    word2 = input().rstrip()

    if word1 == word2 == "END":
        break

    letters = [0 for i in range(26)]

    for letter in word1:
        letters[ord(letter) - ord("a")] += 1

    for letter in word2:
        letters[ord(letter) - ord("a")] -= 1

    for cnt in letters:
        if cnt != 0:
            print(f"Case {index}: different")
            break
    else:
        print(f"Case {index}: same")

    index += 1
