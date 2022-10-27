def count(word, letter):
    count = 0
    for character in word:
        if character == letter:
            count += 1
    print("Number of letters in word: ",count)

inputWord = input("Please input a word: ")
inputLetter = input("Please input a letter: ")
count(inputWord, inputLetter)