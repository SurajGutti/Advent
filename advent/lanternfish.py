"""
suppose you have a lanternfish with an internal timer value of 3:

After one day, its internal timer would become 2.
After another day, its internal timer would become 1.
After another day, its internal timer would become 0.
After another day, its internal timer would reset to 6, and it would create a new lanternfish with an internal timer of 8.
After another day, the first lanternfish would have an internal timer of 5, and the second lanternfish would have an internal timer of 7.

How many lanternfish would there be after 80 days?
"""

from collections import Counter

with open('./inputs/lanternfish.txt', "r") as ip:
    data = [line.strip() for line in ip.readlines()]

data = [int(i) for i in data[0].split(',')]
timers = data.copy()

# print(timers)

# unused counter
for _ in range(0, 80):
    # creating a temporary timer list and a new list to track new fish
    temp = []
    spawned = []
    for t in timers:
        if t == 0:
            spawned.append(8)
            t = 6
        else:
            t -= 1
        temp.append(t)

    temp.extend(spawned)
    timers = temp

print(len(timers))
print(data)

timerCounts = dict(Counter(data))
# timerCounts[6] = timerCounts[7] = timerCounts[-1] = 0

for _ in range(0, 256):
    timerCounts = {l: (0 if timerCounts.get(l + 1) is None else timerCounts.get(l + 1)) for l in range(-1, 8)}
    # make all 8s -1 because we create new fish with 8 after it reaches 0
    timerCounts[8] = timerCounts[-1]
    # add new timers
    timerCounts[6] += timerCounts[-1]
    # reset completed timers
    timerCounts[-1] = 0

# print(timerCounts)

print(sum(timerCounts.values()))
