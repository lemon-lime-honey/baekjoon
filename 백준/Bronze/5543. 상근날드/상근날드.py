burger = list()

for i in range(3):
    burger.append(int(input()))

coke = int(input())
cider = int(input())
cost = list()

for i in range(3):
    case = list()
    case.append(burger[i] + coke - 50)
    case.append(burger[i] + cider - 50)
    cost.append(min(case))

print(min(cost))