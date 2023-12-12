def generatePossibilities(data):
    res = [data]
    for c in data:
        if c == "?":
            newRes = []
            for r in res:
                newRes.append(r.replace("?", "#", 1))
                newRes.append(r.replace("?", ".", 1))
            res = newRes
    return res

def countWorking(poss):
    res = []
    count = 0
    for c in poss:
        if c == "#":
            count += 1
        else:
            if count != 0:
                res.append(count)
            count = 0
    if count != 0:
        res.append(count)
    return res


f = open("in.txt", "r")
lines = f.readlines()

springs = []

for line in lines:
    current = {}
    parts = line.split()
    current["data"] = parts[0]
    current["numbers"] = [int(c) for c in parts[1].split(",")]
    springs.append(current)

res = 0

for spring in springs:
    curr = 0
    poss = generatePossibilities(spring["data"])
    for p in poss:
        counts = countWorking(p)
        if counts == spring["numbers"]:
            curr += 1
    res += curr

print(res)

