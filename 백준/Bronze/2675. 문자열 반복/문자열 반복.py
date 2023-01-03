t = int(input())
repeat = 0
lst = list()
let = ""
temp = ""
total = list()

for i in range(0, t):
    repeat, let = list(map(str, input().split()))
    repeat = int(repeat)
    lst = list(let)
    for j in range(0, len(let)):
        temp += lst[j]*repeat
    total.append(temp)
    let = ""
    lst = list()
    temp = ""

for i in total:
    print(i)
