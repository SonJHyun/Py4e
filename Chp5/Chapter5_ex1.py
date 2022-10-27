count = 0
sum = 0

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        inputNum = float(number)
    except:
        print('Not a number')
        continue
    sum = sum + int(number)
    count += 1

average = str(sum / count)
print('The sum is: ',  sum)
print('The count is: ', count)
print('The average is ',  average)


