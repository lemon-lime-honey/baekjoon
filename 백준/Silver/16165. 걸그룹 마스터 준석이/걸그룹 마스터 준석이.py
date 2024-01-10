import sys
input = sys.stdin.readline

n, m = map(int, input().split())
group = dict()
member = dict()

for i in range(n):
    name = input().rstrip()
    amount = int(input())
    group[name] = set()

    for j in range(amount):
        person = input().rstrip()
        group[name].add(person)
        member[person] = name

for i in range(m):
    question = input().rstrip()
    quiz = int(input())

    if quiz:
        print(member[question])
    else:
        print(*sorted(group[question]), sep='\n')