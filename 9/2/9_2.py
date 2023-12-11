f = open("in.txt", "r")
lines = f.readlines()

def allZero(seq):
    for i in seq:
        if i != 0:
            return False
    return True

def nextSeq(seq):
    new = []
    for i in range(1, len(seq)):
        new.append(seq[i] - seq[i-1])
    return new   

seqs = [[int(x) for x in line.split()] for line in lines]

s = 0

for seq in seqs:
    hist = [seq]
    while not(allZero(hist[-1])):
        hist.append(nextSeq(hist[-1]))
    hist[-1].insert(0, 0)
    for i in range(1, len(hist)):
        hist[len(hist) - i - 1].insert(0,hist[len(hist) - i - 1][0] - hist[len(hist) - i][0])
    s += hist[0][0]

print(s)
