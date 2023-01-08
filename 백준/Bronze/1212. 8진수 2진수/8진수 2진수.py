otob = {'0':'000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}

oct = input()

for i in range(len(oct)):
    if i == 0:
        print(int(otob[oct[i]]), end = '')
    else:
        print(otob[oct[i]], end = '')