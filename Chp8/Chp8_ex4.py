final_list = []
fhand = open('romeo.txt')

for line in fhand:
    words = line.split()
    for word in words:
        if word in final_list:
            continue
        final_list.append(word)

print(sorted(final_list))