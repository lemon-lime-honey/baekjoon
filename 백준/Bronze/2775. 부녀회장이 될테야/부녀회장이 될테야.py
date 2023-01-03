case = int(input())

for i in range(case):
    k = int(input())
    n = int(input())
    num = [x for x in range(1, n+1)]
    
    for j in range(k):
        for l in range(1, n):
            num[l] += num[l-1]
    
    print(num[n-1])