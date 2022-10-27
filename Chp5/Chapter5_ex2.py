from cgi import print_directory


min = None
max = None
count = 0

while True:
    num = input("Enter a number: ")
    
    if num == "done":
        break

    try:
        inputNum = float(num)
    except:
        print("Please input a number: ")
        continue
    
    count += 1
    if min == None and max == None:
        min = num
        max = num
    
    if min > num:
        min = num
    if max < num:
        max = num

print(min)
print(max)
print(count)
        
    


