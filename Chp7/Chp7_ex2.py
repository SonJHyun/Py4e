from this import d


fname = input("Please enter a file name: ")
count = 0
sum = 0
average = 0

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        atPos = line.find(' ')
        floatToFind = line[atPos: ]
        finalFloat = float(floatToFind)
        sum = sum + finalFloat
        count += 1

average = sum / count

fstring = f'Average total is {average}'
print(fstring)