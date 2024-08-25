lyrics = [
    "baby",
    "sukhwan",
    "tururu",
    "turu",
    "very",
    "cute",
    "tururu",
    "turu",
    "in",
    "bed",
    "tururu",
    "turu",
    "baby",
    "sukhwan",
]

n = int(input())

repeat = n // len(lyrics)
target = n % len(lyrics) - 1

match lyrics[target]:
    case "tururu":
        if repeat > 2:
            print(f"tu+ru*{repeat + 2}")
        else:
            print("tururu", "ru" * repeat, sep="")
    case "turu":
        if repeat > 3:
            print(f"tu+ru*{repeat + 1}")
        else:
            print("turu", "ru" * repeat, sep="")
    case _:
        print(lyrics[target])
