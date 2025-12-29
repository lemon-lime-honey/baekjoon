print("n e")
print("- -----------")

result = list()

fact = 1
res = 1

for i in range(10):
    if i != 0:
        fact *= i
        res += 1 / fact
    if i < 2:
        print(f"{i} {int(res)}")
    elif i == 2:
        print(f"{i} {res}")
    else:
        print(f"{i} {res:.9f}")
