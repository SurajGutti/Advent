with open('./inputs/sonarsweep.txt', "r") as ip:
    depthList = ip.readlines()

count = 0

for depth in range(1, len(depthList)):
    if int(depthList[depth-1]) < int(depthList[depth]):
        count += 1

print(count)
