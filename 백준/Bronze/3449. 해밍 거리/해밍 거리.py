t = int(input())

for i in range(t):
    first = input()
    second = input()
    result = 0

    for idx, letter in enumerate(first):
        if second[idx] != letter:
            result += 1

    print(f"Hamming distance is {result}.")
