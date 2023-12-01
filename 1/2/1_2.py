f = open("in.txt", "r")
lines = f.readlines()

sum = 0

for line in lines:
    for i in range(len(line)):
        if line[i].isnumeric():
            first = int(line[i])
            break
        elif line[i] in ["o", "t", "f", "s", "e", "n"]:
            match line[i]:
                case "o":
                    if line[i:i+3] == "one":
                        first = 1
                        break
                case "t":
                    if line[i:i+3] == "two":
                        first = 2
                        break
                    elif line[i:i+5] == "three":
                        first = 3
                        break
                case "f":
                    if line[i:i+4] == "four" :
                        first = 4
                        break
                    elif line[i:i+4] == "five":
                        first = 5
                        break
                case "s":
                    if line[i:i+3] == "six":
                        first = 6
                        break
                    elif line[i:i+5] == "seven":
                        first = 7
                        break
                case "e":
                    if line[i:i+5] == "eight":
                        first = 8
                        break
                case "n":
                    if line[i:i+4] == "nine":
                        first = 9
                        break

    i = len(line) - 1
    while i >= 0:
        print(line[i])
        if line[i].isnumeric():
            last = int(line[i])
            break
        elif line[i] in ["e", "o", "r", "x", "n", "t"]:
            print("there")
            match line[i]:
                case "o":
                    if line[i-2:i+1] == "two":
                        last = 2
                        break
                case "t":
                    if line[i-4:i+1] == "eight":
                        last = 8
                        break
                case "r":
                    if line[i-3:i+1] == "four" :
                        last = 4
                        break
                case "x":
                    if line[i-2:i+1] == "six":
                        last = 6
                        break
                case "e":
                    if line[i-2:i+1] == "one":
                        last = 1
                        break
                    elif line[i-4:i+1] == "three":
                        last = 3
                        break
                    elif line[i-3:i+1] == "five":
                        last = 5
                        break
                    elif line[i-3:i+1] == "nine":
                        last = 9
                        break
                case "n":
                    if line[i-4:i+1] == "seven":
                        last = 7
                        break
        i -= 1
    print((first, last))
    sum += first * 10 + last

print(sum)
    
