def next(coords, map, dir):
    j, i = coords
    if map[i][j] == "-":
        if dir == "r":
            return ((j + 1, i), "r")
        elif dir == "l":
            return ((j - 1, i), "l")
    elif map[i][j] == "|":
        if dir == "u":
            return ((j, i - 1), "u")
        elif dir == "d":
            return ((j, i + 1), "d")
    elif map[i][j] == "L":
        if dir == "d":
            return ((j + 1, i), "r")
        elif dir == "l":
            return ((j, i - 1), "u")
    elif map[i][j] == "J" or map[i][j] == "S":
        if dir == "d":
            return ((j - 1, i), "l")
        elif dir == "r":
            return ((j, i - 1), "u")
    elif map[i][j] == "7":
        if dir == "u":
            return ((j - 1, i), "l")
        elif dir == "r":
            return ((j, i + 1), "d")
    elif map[i][j] == "F":
        if dir == "u":
            return ((j + 1, i), "r")
        elif dir == "l":
            return ((j, i + 1), "d")

f = open("in.txt", "r")
lines = f.readlines()

map = [[c for c in line[:-1]] for line in lines]
highlighted = [line[:] for line in map]

dir = "r"
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "S":
            start = (j, i)

current, dir = next(start, map, dir)
highlighted[start[1]][start[0]] = "X"
while(current != start):
    old = current
    current, dir = next(current, map, dir)
    highlighted[old[1]][old[0]] = "X"

for i in range(len(map)):
    for j in range(len(map[i])):
        if highlighted[i][j] != "X":
            map[i][j] = " "

vertical = ["|", "L", "J", "S"]

res = 0
for i in range(len(map)):
    count = 0
    for j in range(len(map[i])):
        if map[i][j] in vertical:
            count += 1
        elif map[i][j] == " ":
            if count % 2 == 1:
                res += 1

print(res)