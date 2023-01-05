p = int(input())
c = int(input())
b = int(input())
e = int(input())
h = int(input())
g = int(input())

lst1 = [p, c, b, e]
lst2 = [h, g]

lst1.sort(reverse = True)
print(sum(lst1) - lst1[3] + max(lst2))