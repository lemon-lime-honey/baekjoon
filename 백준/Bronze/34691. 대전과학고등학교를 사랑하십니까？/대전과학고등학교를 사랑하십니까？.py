while True:
    ipt = input()

    if ipt == "end":
        break
    
    match ipt:
        case "animal":
            print("Panthera tigris")
        case "tree":
            print("Pinus densiflora")
        case "flower":
            print("Forsythia koreana")
