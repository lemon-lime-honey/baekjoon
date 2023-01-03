lst = list()
while(1):
    try:
        lst.append(int(input()))
    except:
        break

print(max(lst))
print(lst.index(max(lst))+1)