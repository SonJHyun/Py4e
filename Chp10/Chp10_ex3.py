import string
chars = dict()

fname = input("Please enter a file name: ")

try:
    fhand = open(fname, encoding='utf-8')
except:
    print("File cannot be opened:", fname)
    exit()


for line in fhand:
    line = line.strip()
    line = line.lower()
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.replace(' ', '')

    for char in line:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1


chars_list = list()

for key, val in list(chars.items()):
    chars_list.append((key, val))

chars_list.sort()
print(chars_list)