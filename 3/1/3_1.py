f = open("in.txt", "r")
lines = f.readlines()

m = [[c for c in line] for line in lines]
sum = 0

for i in range(len(m)):
    j = 0
    while j < len(m[0]) - 1:
        if m[i][j].isnumeric():
            symbols = []
            l = 1
            if j + 1 < len(m[0]) - 1 and m[i][j + 1].isnumeric():
                l = 2
                if j + 2 < len(m[0]) - 1 and m[i][j + 2].isnumeric():
                    l = 3
            miny = max(0, i - 1)
            maxy = min(i + 1, len(m) - 1)
            minx = max(0, j - 1)
            maxx = min(j + l, len(m[0]) - 2)
            
            for a in range(miny, maxy + 1):
                for b in range(minx, maxx + 1):
                    symbols.append(m[a][b])

            if(len(set([i for i in symbols if not i.isnumeric() and i != "."])) > 0):
                sum += int("".join(m[i][j:j+l]))
            j += l + 1
        else:
            j += 1
    
print(sum)
    