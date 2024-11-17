n, m = map(int, input().split())
lst = list()
result = True

for i in range(n):
    ipt = input()
    word = list()
    for letter in ipt:
        word.append(letter)
        word.append(letter)
    lst.append("".join(word))

for i in range(n):
    ipt = input()
    if ipt != lst[i]:
        result = False

print("Eyfa" if result else "Not Eyfa")
