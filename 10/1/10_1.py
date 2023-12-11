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

dir = "r"
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "S":
            start = (j, i)

dist = 1
current, dir = next(start, map, dir)
while(current != start):
    dist += 1
    current, dir = next(current, map, dir)

print(dist // 2)

            