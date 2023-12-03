f = open("in.txt", "r")
lines = f.readlines()

max = {"red": 12, "green": 13, "blue": 14}
sum = 0

for line in lines:
    parts = line.split(":")
    num = int(parts[0].split()[1])
    games = parts[1].split(";")
    possible = True
    for game in games:
        colors = game.split(",")
        for color in colors:
            p = color.split()
            a, c = int(p[0]), p[1]
            if a > max[c]:
                possible = False
    if possible:
        sum += num

print(sum)
