with open('./inputs/whale.txt', "r") as ip:
    data = [line.strip() for line in ip.readlines()]

positions = [int(i) for i in data[0].split(',')]

f = []

for pos in range(0, len(positions)):
    pos_diff = []
    # calculating the total fuel required for every crab to reach every possible position
    for each in positions:
        pos_diff.append(abs(each - pos))

    # get exponential sums of moving to each of the possible locations within the range (max/min of the crabs farthest)
    # very bad solution
    all_moves = []
    for n in pos_diff:
        all_moves.append(sum(list(range(n+1))))

    total = sum(all_moves)
    f.append(total)

print(min(f))