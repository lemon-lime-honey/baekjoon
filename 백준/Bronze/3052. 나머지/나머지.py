from collections import Counter

lst = list()
for i in range(0, 10):
    lst.append(int(input()))
    lst[i] = lst[i]%42

print(len(Counter(lst).keys()))
