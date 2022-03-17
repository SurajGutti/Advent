with open('./inputs/binary.txt', "r") as ip:
    report = ip.readlines()

bSize = len(report[0])
bPos = {}
for i in range(0, bSize-1):
    bPos[i + 1] = [0, 0]

for val in report:
    for i in range(0, len(val)):
        if not val[i].isdigit(): continue
        if int(val[i]) == 0:
            bPos[i + 1][0] += 1
        elif int(val[i]) == 1:
            bPos[i + 1][1] += 1

gr, er = "", ""

for i in range(1, bSize):
    # print(bPos[i][0],bPos[i][0])
    if bPos[i][0] > bPos[i][1]:
        gr += "0"
        er += "1"
    else:
        gr += "1"
        er += "0"

print(gr)
print(er)
print(int(gr, 2)*int(er, 2))
print(bPos)
