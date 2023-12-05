f = open("in.txt", "r")
lines = f.readlines()

def readMapping(data, start, end):
    return [{"dest": int(line.split()[0]), "source": int(line.split()[1]), "length": int(line.split()[2])} for line in data[start:end]]

def convert(data, mapping):
    converted = []
    for d in data:
        res = None
        for conv in mapping:
            if d >= conv["source"] and d <= conv["source"] + conv["length"]:
                res = conv["dest"] + d - conv["source"]
                break
        if res == None:
            res = d
        converted.append(res)
    return converted

seeds = [int(x) for x in lines[0].split()[1:]]
seedToSoil = readMapping(lines, 3, 21)
soilToFert = readMapping(lines, 23, 31)
fertToWater = readMapping(lines, 33, 68)
waterToLight = readMapping(lines, 70, 115)
lightToTemp = readMapping(lines, 117, 131)
tempToHum = readMapping(lines, 133, 161)
humToLoc = readMapping(lines, 163, 174)

soils = convert(seeds, seedToSoil)
fert = convert(soils, soilToFert)
water = convert(fert, fertToWater)
light = convert(water, waterToLight)
temp = convert(light, lightToTemp)
hum = convert(temp, tempToHum)
loc = convert(hum, humToLoc)

print(min(loc))