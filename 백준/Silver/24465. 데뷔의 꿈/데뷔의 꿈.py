import sys


def find(month, day):
    match month:
        case 1:
            if day < 20:
                return "capricorn"
            return "aquarius"
        case 2:
            if day < 19:
                return "aquarius"
            return "pisces"
        case 3:
            if day < 21:
                return "pisces"
            return "aries"
        case 4:
            if day < 20:
                return "aries"
            return "taurus"
        case 5:
            if day < 21:
                return "taurus"
            return "gemini"
        case 6:
            if day < 22:
                return "gemini"
            return "cancer"
        case 7:
            if day < 23:
                return "cancer"
            return "leo"
        case 8:
            if day < 23:
                return "leo"
            return "virgo"
        case 9:
            if day < 23:
                return "virgo"
            return "libra"
        case 10:
            if day < 23:
                return "libra"
            return "scorpio"
        case 11:
            if day < 23:
                return "scorpio"
            return "sagittarius"
        case 12:
            if day < 22:
                return "sagittarius"
            return "capricorn"



input = sys.stdin.readline
members = sorted([list(map(int, input().split())) for i in range(7)])
result = list()
n = int(input())

zodiac = {
    "aquarius",
    "pisces",
    "aries",
    "taurus",
    "gemini",
    "cancer",
    "leo",
    "virgo",
    "libra",
    "scorpio",
    "sagittarius",
    "capricorn",
}

for month, day in members:
    zodiac.discard(find(month, day))

for i in range(n):
    month, day = map(int, input().split())
    if find(month, day) in zodiac:
        result.append((month, day))

result.sort()

if not result:
    print("ALL FAILED")
else:
    for month, day in result:
        print(month, day)
