with open('./inputs/sonarsweep.txt', "r") as ip:
    depthList = [int(val) for val in ip]

count = 0

for d in range(3, len(depthList)):
    prev, curr = depthList[d - 3] + depthList[d - 2] + depthList[d - 1], depthList[d - 2] + depthList[d - 1] + depthList[d]
    if prev < curr:
        count += 1

print(count)
