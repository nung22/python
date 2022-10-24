# 1.Countdown
def countdown(num):
    cdown = []
    for x in range(num,-1,-1):
        cdown.append(x)
    return cdown
print(countdown(5))


# 2.Print and Return
def print_and_return(pair):
    print(pair[0])
    return pair[1]
print(print_and_return([1,2]))


# 3.First Plus Length
def first_plus_length(nList):
    return nList[0] + len(nList)
print(first_plus_length([1,2,3,4,5]))


# 4.Values Greater than Second
def values_greater_than_second(nList):
    if len(nList) < 2:
        return False
    else:
        newList = []
        for x in nList:
            if x > nList[1]:
                newList.append(x)
        print(len(newList))
        return newList
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


# 5.This Length, That Value
def length_and_value(size,value):
    newList = []
    for x in range(size):
        newList.append(value)
    return newList
print(length_and_value(4,7))
print(length_and_value(6,2))