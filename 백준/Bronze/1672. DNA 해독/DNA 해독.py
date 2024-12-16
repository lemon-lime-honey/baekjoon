n = int(input())
ipt = input()
result = ipt[-1]

for i in range(n - 2, -1, -1):
    match result:
        case "A":
            match ipt[i]:
                case "A":
                    result = "A"
                case "G":
                    result = "C"
                case "C":
                    result = "A"
                case "T":
                    result = "G"
        case "G":
            match ipt[i]:
                case "A":
                    result = "C"
                case "G":
                    result = "G"
                case "C":
                    result = "T"
                case "T":
                    result = "A"
        case "C":
            match ipt[i]:
                case "A":
                    result = "A"
                case "G":
                    result = "T"
                case "C":
                    result = "C"
                case "T":
                    result = "G"
        case "T":
            match ipt[i]:
                case "A":
                    result = "G"
                case "G":
                    result = "A"
                case "C":
                    result = "G"
                case "T":
                    result = "T"

print(result)
