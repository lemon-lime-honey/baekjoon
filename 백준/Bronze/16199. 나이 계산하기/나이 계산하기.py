birth = list(map(int, input().split()))
ref = list(map(int, input().split()))
age = ref[0] - birth[0]
if (birth[1] < ref[1]) + (birth [1] == ref[1]) * (birth[2] <= ref[2]):
    print(ref[0] - birth[0])
else:
    print(age - 1)
print(age + 1)
print(age)