from time import time


fname = open("mbox-short.txt")
hours_count = dict()

for line in fname:
    line = line.rstrip()
    if not line.startswith('From '): continue

    words = line.split()

    time_full = words[5]
    at_pos = time_full.find(':')
    
    hours = time_full[:at_pos]

    if hours not in hours_count:
        hours_count[hours] = 1
    else:
        hours_count[hours] += 1

hours_list = list()

for key, val in list(hours_count.items()):
    hours_list.append((key, val))

hours_list.sort()

print(hours_list)
