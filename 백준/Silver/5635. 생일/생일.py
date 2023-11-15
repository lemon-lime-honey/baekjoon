n = int(input())
student = dict()

for i in range(n):
    ipt = input().split()
    student[ipt[0]] = tuple(map(int, ipt[1:]))

data = sorted(student.items(), key=lambda x:(x[1][2], x[1][1], x[1][0]))
print(data[-1][0], data[0][0], sep='\n')