from audioop import add


fname = open("mbox-short.txt")
num_messages = dict()

for line in fname:
    line = line.rstrip()
    if not line.startswith('From '): continue

    words = line.split()
    
    address = words[1]
    if address not in num_messages:
        num_messages[address] = 1
    else:
        num_messages[address] += 1

lst = list()
for key, val in list(num_messages.items()):
    lst.append((key, val))

lst.sort(reverse=True)

for key, val in lst[:]:
    print(key, val)
