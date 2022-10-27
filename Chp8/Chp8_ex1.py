t = [1,2,3,4,5]

def chop(list):
    del list[0]
    del list[len(list) - 1]

chop(t)
print(t)