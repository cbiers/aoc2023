f = open("in.txt", "r")
lines = f.readlines()

def readMapping(data, start, end):
    return [{"dest": int(line.split()[0]), "source": int(line.split()[1]), "length": int(line.split()[2])} for line in data[start:end]]

def revert(num, mapping):
    res = None
    for conv in mapping:
        if num >= conv["dest"] and num <= conv["dest"] + conv["length"]:
            res = conv["source"] + num - conv["dest"]
            break
    if res == None:
        res = num
    return res

seedNums = [int(x) for x in lines[0].split()[1:]]
i = 0
seeds = []
while i < len(seedNums):
    seeds.append({"start": seedNums[i], "length": seedNums[i + 1]})
    i += 2

seedToSoil = readMapping(lines, 3, 21)
soilToFert = readMapping(lines, 23, 31)
fertToWater = readMapping(lines, 33, 68)
waterToLight = readMapping(lines, 70, 115)
lightToTemp = readMapping(lines, 117, 131)
tempToHum = readMapping(lines, 133, 161)
humToLoc = readMapping(lines, 163, 174)

done = False
i = 0
while not done:
    if i % 1000000 == 0:
        print(i)
    hum = revert(i, humToLoc)
    temp = revert(hum, tempToHum)
    light = revert(temp, lightToTemp)
    water = revert(light, waterToLight)
    fert = revert(water, fertToWater)
    soil = revert(fert, soilToFert)
    seed = revert(soil, seedToSoil)
    for s in seeds:
        if seed >= s["start"] and seed <= s["start"] + s["length"]:
            print(i)
            done = True
            break
    i += 1