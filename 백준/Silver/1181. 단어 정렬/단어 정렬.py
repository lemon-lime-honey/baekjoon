num = int(input())
word = list()
for i in range(num):
    temp = input()
    if temp not in word:
        word.append(temp)

word.sort(key = lambda x: (len(x), x))

for item in word:
    print(item)