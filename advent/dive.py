with open('./inputs/dive.txt', "r") as ip:
    commands = ip.readlines()

pos, depth = 0, 0

for ip in commands:
    val = int(ip[-2])
    if "forward" in ip:
        pos += val
    elif "down" in ip:
        depth += val
    elif "up" in ip:
        depth -= val

print(pos*depth)