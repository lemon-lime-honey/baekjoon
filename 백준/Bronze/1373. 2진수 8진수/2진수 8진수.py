btoo = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', 
'110': '6', '111': '7'}

binary = input()
length = len(binary)

if length % 3 == 1:
    binary = '00' + binary
elif length % 3 == 2:
    binary = '0' + binary

for i in range(0, length, 3):
    print(btoo[binary[i : i+3]], end ='')