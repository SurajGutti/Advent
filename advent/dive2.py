with open('./inputs/dive.txt', "r") as ip:
    commands = ip.readlines()

pos, depth, aim = 0, 0, 0

for ip in commands:
    val = int(ip[-2])
    if "forward" in ip:
        pos += val
        depth += aim*val
    elif "down" in ip:
        aim += val
    elif "up" in ip:
        aim -= val

print(pos*depth)