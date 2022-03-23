"""
An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap.
In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
"""

import re
import numpy as np

with open('./inputs/vents.txt', 'r') as ip:
    lines = ip.readlines()

re_lines = []

# reformat each line to fit the template [x1, y1, x2, y2]
for line in lines:
    ref = (re.sub('[^0-9]', ' ', line).split())
    ref = list(map(int, ref))
    re_lines.append(ref)

print(re_lines)

# used to create an array (field)
cols, rows = 0, 0

for line in re_lines:
    x1, y1, x2, y2 = line
    cols = max(cols, x1, x2)
    rows = max(rows, y1, y2)

print("Grid: " + str(rows) + " x " + str(cols))

# build the grid with 0s
vent_grid = np.zeros((rows + 1, cols + 1), dtype=int)


# function that increases the value of the [x,y] per horizontal or vertical lines
def add_straight_line(grid, x1, y1, x2, y2):
    if x1 == x2:
        for y_co in range(min(y1, y2), max(y1, y2) + 1):
            grid[y_co, x1] += 1
        return
    if y1 == y2:
        for x_co in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1, x_co] += 1
        return


def add_diagonal_lines(grid, x1, y1, x2, y2):
    line_length = abs(x1 - x2) + 1

    # x and y always increases or decreases by 1 since the angle is 45
    # to check whether the counter increases or decreases (the co-ordinate increases or decreases)
    x_counter = 1 if x2 - x1 > 0 else -1
    y_counter = 1 if y2 - y1 > 0 else -1

    for i in range(0, line_length):
        curr_x = x1 + i * x_counter
        curr_y = y1 + i * y_counter
        # because the line is diagonal, the line goes up or down
        grid[curr_y, curr_x] += 1


# draw the lines
for line in re_lines:
    x1, y1, x2, y2 = line
    if x1 == x2 or y1 == y2:
        add_straight_line(vent_grid, x1, y1, x2, y2)
    else:
        add_diagonal_lines(vent_grid, x1, y1, x2, y2)

# count the total values >= 2
count = (vent_grid >= 2).sum()
print(count)
