from datetime import date

def solution(date1, date2):
    one = date(year=date1[0], month=date1[1], day=date1[2])
    two = date(date2[0], date2[1], date2[2])
    return 1 if one < two else 0