t = int(input())
lst = list()
score = list()
total = list()
num = 0
count = 0
temp = 0

for i in range(0, t):
    lst = list(input())
    
    for j in range(0, len(lst)):
        if (lst[j]=='O'):
            count += 1
            num += count
        else:
            score.append(num)
            count = 0
            num = 0
            
    score.append(num)
    count = 0
    num = 0

    for j in score:
        temp += j
        
    total.append(temp)
    lst = list()
    score = list()
    temp = 0

for i in total:
    print(i)
