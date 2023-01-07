from datetime import date

name = {0: 'MON', 1: 'TUE', 2: 'WED', 3: 'THU', 4: 'FRI', 5: 'SAT', 6: 'SUN'}

x, y = map(int, input().split())
print(name[date(2007, x, y).weekday()])