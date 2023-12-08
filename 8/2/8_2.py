from math import gcd

f = open("in.txt", "r")
lines = f.readlines()

def lcm(l):
    lcm = 1
    for s in l:
        lcm = lcm * s // gcd(lcm, s)
    return lcm

instructions = lines[0][:-1]
maps = {}

for line in lines[2:]:
    parts = line.split()
    maps[parts[0]] = {"left": parts[2][1:-1], "right": parts[3][:-1]}

current = [key for key in maps.keys() if key[-1] == "A"]

steps = []

for i in range(len(current)):   
    currstep = 0
    while current[i][-1] != "Z":
        instruction = instructions[currstep % len(instructions)]
        if instruction == "L":
            current[i] = maps[current[i]]["left"]
        else:
            current[i] = maps[current[i]]["right"]
        currstep += 1
    steps.append(currstep)

print(lcm(steps))