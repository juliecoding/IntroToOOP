import functools

filename = input("Enter the input file name: numbers.txt")
fileToString = '';

with open(filename) as f:
    for line in f:
        fileToString += line
    toList = fileToString.split()
    numbers = list(map(int, toList))
    total = functools.reduce(lambda acc, cv: acc + cv, numbers)
    print("The average is", total / len(numbers))

