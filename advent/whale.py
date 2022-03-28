"""
Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible.
This means there's a crab with horizontal position 16, a crab with horizontal position 1, and so on.

Each change of 1 step in horizontal position of a single crab costs 1 fuel.
You could choose any horizontal position to align them all on, but the one that costs the least fuel is horizontal position 2

Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?
"""

with open('./inputs/whale.txt', "r") as ip:
    data = [line.strip() for line in ip.readlines()]

positions = [int(i) for i in data[0].split(',')]

f = []

# calculating the total fuel required for every crab to reach every possible position
# and getting its minimum
for pos in range(0, len(positions)):
    total = []
    for each in positions:
        total.append(abs(each - pos))
    f.append(sum(total))

print(min(f))
