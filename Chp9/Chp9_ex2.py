file = open("mbox-short.txt")
whichDay = dict()


for line in file:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()

    day = words[2]
    print(day)
    

    if day not in whichDay:
        whichDay[day] = 1
    else:
        whichDay[day] += 1

print(whichDay)