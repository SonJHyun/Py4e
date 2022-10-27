file = open("words.txt")
fruits = dict()

for word in file:
    word = word.rstrip()
    fruits[word] = "is a fruit"

print(fruits)