n = int(input())
people = set()
flag = False

for i in range(n):
    a, b = input().split()
    if flag:
        if a in people: people.add(b)
        if b in people: people.add(a)
    else:
        if a == 'ChongChong' or b == 'ChongChong':
            people.add(a)
            people.add(b)
            flag = True

print(len(people))