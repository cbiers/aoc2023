f = open("in.txt", "r")
lines = f.readlines()

res = 1

times = [int(time) for time in lines[0].split(":")[1].split()]
dists = [int(dist) for dist in lines[1].split(":")[1].split()]

for i in range(len(times)):
    beat = 0
    time = times[i]
    for j in range(1, time + 1):
        travel = j * (time - j)
        if travel > dists[i]:
            beat += 1
    res *= beat

print(times)
print(dists)
print(res)
