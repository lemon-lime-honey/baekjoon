total = int(input())
num = int(input())
lst = list[num]
result = 0

for i in range(num):
    temp = list(map(int, input().split()))
    result += temp[0] * temp[1]

if (total == result):
    print("Yes")
else:
    print("No")