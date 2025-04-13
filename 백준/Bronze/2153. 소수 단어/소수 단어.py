prime = [True for i in range(1041)]
prime[0] = False

for i in range(2, int(1041 ** 0.5) + 1):
    if prime[i]:
        for j in range(2 * i, 1041, i):
            prime[j] = False

word = input()
num = 0

for letter in word:
    if letter.isupper():
        num += ord(letter) - ord("A") + 27
    else:
        num += ord(letter) - ord("a") + 1

if prime[num]:
    print("It is a prime word.")
else:
    print("It is not a prime word.")
