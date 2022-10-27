fname = input("Please enter a file name: ")

try:
    fhand = open(fname, encoding='utf-8')
except:
    print("File cannot be opened:", fname)
    exit()


for line in fhand:
    line = line.strip()
    line = line.lower()

    print(line)


