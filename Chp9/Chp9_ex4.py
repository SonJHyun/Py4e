fname = input('Please input a file name: ')

emails = dict()
max = 0
max_email = ''

try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fhand)

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()

    email = words[1]
    
    if email not in emails:
        emails[email] = 1
    else:
        emails[email] += 1

for address in emails:
    if emails[address] > max:
        max = emails[address]
        max_email = address

print(max_email, max)