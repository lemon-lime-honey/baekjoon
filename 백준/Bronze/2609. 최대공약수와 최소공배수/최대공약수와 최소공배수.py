num = list(map(int, input().split()))
temp1 = num[0]
temp2 = num[1]
while (temp2 != 0):
    temp1, temp2 = temp2, (temp1 % temp2)

print(temp1)
print(int(num[0] * num[1] / temp1))