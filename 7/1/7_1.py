cardValues = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7" : 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q":12, "K": 13, "A": 14}

def getValue(hand):
    eval = {}
    for card in hand:
        if card in eval:
            eval[card] += 1
        else:
            eval[card] = 1
    if 5 in eval.values():
        return 7
    if 4 in eval.values():
        return 6
    if 3 in eval.values() and 2 in eval.values():
        return 5
    if 3 in eval.values():
        return 4
    if len(eval) == 3:
        return 3
    if len(eval) == 4:
        return 2
    return 1

def compareCards(card1, card2):
    if cardValues[card1[0]] > cardValues[card2[0]]:
        return 1
    elif cardValues[card1[0]] < cardValues[card2[0]]:
        return -1
    return 0

def compareHands(hand1, hand2):
    if hand1["value"] > hand2["value"]:
        return 1
    if hand1["value"] < hand2["value"]:
        return -1
    for i in range(5):
        if compareCards(hand1["hand"][i], hand2["hand"][i]) == 1:
            return 1
        if compareCards(hand1["hand"][i], hand2["hand"][i]) == -1:
            return -1
    return 1

def sortHands(hands):
    for i in range(len(hands)):
        for j in range(i + 1, len(hands)):
            if compareHands(hands[i], hands[j]) == 1:
                hands[i], hands[j] = hands[j], hands[i]
    return hands
    
f = open("in.txt", "r")
lines = f.readlines()

hands = []
for line in lines:
    parts = line.split()
    hands.append({"hand": parts[0], "bid": int(parts[1]), "value": getValue(parts[0])})

sum = 0

hands = sortHands(hands)
print(hands)

for i in range(len(hands)):
    sum += hands[i]["bid"] * (i + 1)

print(sum)