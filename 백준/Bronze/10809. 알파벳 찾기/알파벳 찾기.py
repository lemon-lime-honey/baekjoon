s = input()
alphabet = list(map(chr, range(97, 123)))
location = list()

for i in alphabet:
    location.append(s.find(i))
    
for i in range(0, 26):
    print(location[i], end = ' ')
