from functools import reduce

def add(x, y):
    return x + y

fileName = input("enter the file input name")
inputFile = open(fileName, 'r')

myList = []

for line in inputFile:
    myList.extend(line.split())

myList = list(map(float, myList))

# total = reduce(add, myList)
total = reduce(lambda x, y : x + y, myList)
average = total / len(myList)
print("The average is ", average)


#numbers.txt =
#45 66 68

