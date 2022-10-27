'''


fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])

'''
#if the first word is from but second word is non-existent then program will fail
#we can check for this condition as well to fix this issue

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 3: continue
    if words[0] != 'From' : continue
    print(words[2])