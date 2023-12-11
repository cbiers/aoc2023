f = open("in.txt", "r")
lines = f.readlines()

map = [[c for c in line.strip()] for line in lines]

i = len(map) - 1
while i >= 0:
    if "#" not in map[i]:
        map.insert(i, ["." for j in range(len(map[0]))])
    i -= 1

i = len(map[0]) - 1
while i >= 0:
    if "#" not in [row[i] for row in map]:
        for row in map:
            row.insert(i, ".")
    i -= 1

coords = []
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "#":
            coords.append((i, j))

sum = 0
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        sum += abs(coords[i][0] - coords[j][0]) + abs(coords[i][1] - coords[j][1])

print(sum)