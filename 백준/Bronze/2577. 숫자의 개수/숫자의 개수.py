a = int(input())
b = int(input())
c = int(input())

result = a*b*c
lst = list(map(int, str(result)))

for i in range(0, 10):
    print(lst.count(i))