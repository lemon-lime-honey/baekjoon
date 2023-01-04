month = int(input())
day = int(input())

if (month == 2) * (day == 18):
    print('Special')
elif (month > 2) + ((month == 2) * (day > 18)):
    print('After')
else:
    print('Before')