n = int(input())
people = dict()

for i in range(n):
    log = input().split()
    if log[1] == 'enter':
        people[log[0]] = 1
    elif log[1] == 'leave':
        people.pop(log[0], 0)

result = list(people.keys())
result.sort(reverse = True)

for name in result:
    print(name)