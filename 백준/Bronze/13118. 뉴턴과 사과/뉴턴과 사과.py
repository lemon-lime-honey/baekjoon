people = list(map(int, input().split()))
apple = list(map(int, input().split()))
flag = 0

for i in range(4):
    if people[i] == apple[0]:
        flag = 1
        print(i + 1)
if flag == 0:
    print(0)