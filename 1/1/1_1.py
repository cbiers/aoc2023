f = open("in.txt", "r")
lines = f.readlines()

sum = 0

for line in lines:
    for char in line:
        if char.isnumeric():
            first = int(char)
            break
    i = len(line) - 1
    while i >= 0:
        if line[i].isnumeric():
            last = int(line[i])
            break
        i -= 1
    sum += first * 10 + last

print(sum)
    
