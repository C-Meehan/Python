#Countdown
def countdown(num):
    countlist = []
    for i in range(num,-1,-1):
        countlist.append(i)
    return countlist
print(countdown(5))

#Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2]))

#First plus length
def first_plus_length(list):
    return list[0] + len(list)
    
print(first_plus_length([1,2,3,4,5]))
    
#Values greater than second
def values_greater_than_second(list):
    if (len(list) < 2):
        return False
    else: 
        newList = []
        numsGreater = 0
        for i in range(0,len(list),1):
            if (list[i] > list[1]):
                numsGreater = numsGreater + 1
                newList.append(list[i])
                # print(newList)
    print(numsGreater)
    return newList

print(values_greater_than_second([5,2,3,2,1,4]))

#This Length, That Value
def length_and_value(size, value):
    empty = []
    for i in range(0,size,1):
        empty.append(value)
    # print(empty)
    return empty

print(length_and_value(4,7))


