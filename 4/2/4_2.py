f = open("in.txt", "r")
lines = f.readlines()

cards = []
queue = []

counter = 1
for line in lines:
    winning, drawn = line.split(":")[1].split("|")
    winning = winning.split()
    drawn = drawn.split()
    matches = len(set(winning).intersection(drawn))

    cards.append({"matches": matches, "count": 1})
    queue.append(counter)
    counter += 1

while len(queue) > 0:
    curr = queue.pop()
    match = cards[curr - 1]["matches"]
    for i in range(1, match + 1):
        cards[curr + i - 1]["count"] += 1
        queue.append(curr + i)

print(sum([card["count"] for card in cards]))