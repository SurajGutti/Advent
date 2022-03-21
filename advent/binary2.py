with open('./inputs/binary.txt', 'r') as f:
    lines = f.readlines()
    result = [entry.strip() for entry in lines]

from copy import copy

oxy = copy(result)
co2 = copy(result)

for i in range(len(result[0])):
    if len(oxy) == 1:
        break
    all_entries_at_pos = [entry[i] for entry in oxy]
    common_bit = '1' if all_entries_at_pos.count('1') >= len(oxy) / 2 else '0'
    oxy = [entry for entry in oxy if entry[i] == common_bit]
oxygen_rating = int(oxy[0], 2)
print(oxy[0], oxygen_rating)

for i in range(len(result[0])):
    if len(co2) == 1:
        break
    all_entries_at_pos = [entry[i] for entry in co2]
    least_common_bit = '0' if all_entries_at_pos.count('1') >= len(co2) / 2 else '1'
    co2 = [entry for entry in co2 if entry[i] == least_common_bit]
co2_rating = int(co2[0], 2)

print(oxygen_rating * co2_rating)
