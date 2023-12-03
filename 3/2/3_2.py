def getAdjacentNumbers(m, i, j):
    res = []
    minY = max(0, i - 1)
    maxY = min(i + 1, len(m) - 1)
    minX = max(0, j - 1)
    maxX = min(j + 1, len(m[j]) - 2)
    for k in range(minY, maxY + 1):
        lineres = []
        for l in range(minX, maxX + 1):
            if m[k][l].isnumeric():
                minC = max(0, l - 2)
                maxC = min(l + 2, len(m[l]) - 2) 
                curr = []
                for e in range(minC, maxC + 1):
                    if m[k][e].isnumeric():
                        curr.append(m[k][e])
                    elif e < l:
                        curr = []
                    else:
                        break
                    if len(curr) == 3:
                        break
                if len(curr) > 0:
                    currNum = 0
                    for i in range(len(curr)):
                        currNum *= 10
                        currNum += int(curr[i])
                    if currNum not in lineres:
                        lineres.append(currNum)     
        res.extend(lineres)                  
    return res

f = open("in.txt", "r")
lines = f.readlines()

m = [[c for c in line] for line in lines]
sum = 0

i = 0
while i < len(m):
    j = 0
    while j < len(m[i]) - 1:
        if(m[i][j] == "*"):
            adj = getAdjacentNumbers(m, i, j)
            if len(adj) == 2:
                sum += adj[0] * adj[1]
        j += 1
    i += 1
    
print(sum)
    