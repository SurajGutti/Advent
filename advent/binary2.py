with open('./inputs/binary.txt', "r") as ip:
    report = ip.readlines()

bSize = len(report[0])
bPos = {}
for i in range(0, bSize - 1):
    bPos[i + 1] = [0, 0]

for val in report:
    for i in range(0, len(val)):
        if not val[i].isdigit(): continue
        if int(val[i]) == 0:
            bPos[i + 1][0] += 1
        elif int(val[i]) == 1:
            bPos[i + 1][1] += 1

oxr = report

for i in range(0, len(bPos)):

    if bPos[i + 1][0] > bPos[i + 1][1]:
        mVal = "0"
    else:
        mVal = "1"

    for val in oxr:
        if not val[i] == mVal:
            oxr.remove(val)

print(oxr)