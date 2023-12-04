f = open("in.txt", "r")
lines = f.readlines()

sum = 0

for line in lines:
    winning, drawn = line.split(":")[1].split("|")
    winning = winning.split()
    drawn = drawn.split()
    
    curr = 0
    for d in drawn:
        if d in winning:
            curr += 1
    if curr > 0:
        sum += 2 ** (curr - 1)

print(sum)
