word = input().upper()
alphabet = list(map(chr, range(65, 91)))
num = list()

for i in alphabet:
    temp = word.count(i)
    num.append(temp)
    
maxNum = max(num)

if num.count(maxNum)==1:
    print(alphabet[num.index(maxNum)])
else:
    print("?")
