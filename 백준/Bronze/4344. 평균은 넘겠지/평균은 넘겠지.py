c = int(input())
lst = list()
people = 0
numSum = 0
avg = 0
howmany = 0
avgLst = list()

for i in range(0, c):
    lst = list(map(int, input().split()))
    people = lst.pop(0)
    for j in lst:
        numSum += j
    avg = numSum/people
    for j in lst:
        if j>avg:
            howmany += 1
    avgLst.append(100*howmany/people)
    lst = list()
    people = 0
    numSum = 0
    avg = 0
    howmany = 0

for i in avgLst:
    print("{0:0.3f}%".format(i))
