f = open("in.txt", "r")
lines = f.readlines()

sum = 0

for line in lines:
    parts = line.split(":")
    games = parts[1].split(";")
    curr = {"red": 0, "green": 0, "blue": 0}
    for game in games:
        colors = game.split(",")
        for color in colors:
            p = color.split()
            a, c = int(p[0]), p[1]
            curr[c] = max(curr[c], a)
    sum += curr["red"] * curr["blue"] * curr["green"]

print(sum)
