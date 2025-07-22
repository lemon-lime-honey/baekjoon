from datetime import date

day, month = map(int, input().split())
target = date(year=2009, month=month, day=day)

match target.weekday():
    case 0:
        print("Monday")
    case 1:
        print("Tuesday")
    case 2:
        print("Wednesday")
    case 3:
        print("Thursday")
    case 4:
        print("Friday")
    case 5:
        print("Saturday")
    case 6:
        print("Sunday")
