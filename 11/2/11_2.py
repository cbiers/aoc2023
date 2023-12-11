def emptyRows(i, j, m):
    count = 0
    i, j = min(i, j), max(i, j)
    for k in range(i + 1, j):
        if "#" not in map[k]:
            count += 1
    return count

def emptyColumns(i, j, m):
    count = 0
    i, j = min(i, j), max(i, j)
    for k in range(i + 1, j):
        if "#" not in [row[k] for row in map]:
            count += 1
    return count

f = open("in.txt", "r")
lines = f.readlines()

map = [[c for c in line.strip()] for line in lines]

coords = []
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "#":
            coords.append((i, j))

sum = 0
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        toAdd = emptyColumns(coords[i][1], coords[j][1], map) + emptyRows(coords[i][0], coords[j][0], map)
        sum += abs(coords[i][0] - coords[j][0]) + abs(coords[i][1] - coords[j][1]) + toAdd * 999999

print(sum)