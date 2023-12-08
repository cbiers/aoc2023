f = open("in.txt", "r")
lines = f.readlines()

instructions = lines[0][:-1]
maps = {}

for line in lines[2:]:
    parts = line.split()
    maps[parts[0]] = {"left": parts[2][1:-1], "right": parts[3][:-1]}

current = "AAA"
steps = 0

while current != "ZZZ":
    instruction = instructions[steps % len(instructions)]
    if instruction == "L":
        current = maps[current]["left"]
    else:
        current = maps[current]["right"]
    steps += 1

print(steps)