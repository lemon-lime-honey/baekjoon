t = int(input())

for i in range(t):
    n = int(input())
    result = 0
    school = ''

    for j in range(n):
        ipt = list(input().split())
        if int(ipt[-1]) > result:
            result = int(ipt[-1])
            school = ipt[0]

    print(school)