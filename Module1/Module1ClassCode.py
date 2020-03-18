import sys


def square(x):
    """Returns the square of x."""
    return x * x


def addList(lst):
    sum = 0
    for n in lst:
        sum += n
    return sum


def addListRecursively(lst):
    # 1 BASE CASE
    if len(lst) == 1:  # OR, if not lst: return 0
        return lst[0]
    # 2 DIMINISHING VALUE
    truncatedList = lst[1:]
    # 3 RECURSIVE CASE
    return lst[0] + addListRecursively(truncatedList)


def displayRange(lower, upper):
    if lower <= upper:
        print(lower)
        displayRange(lower + 1, upper)


def main():
    myList = [1, 2, 3, 4, 5]
    totalSum = addList(myList)
    print(totalSum)

    def defaultValueFunc(x, y=5, z=10):
        if y == 5:
            return x * y / z
        return 6 > 5

    # print("hello world")
    # print(help(square))
    # print(square(5))
    # print(defaultValueFunc(6, 10))

    print(sys.argv[0])
    print(sys.argv[1])

# local variables: where in memory do those live?

def changeValue(x):
    x = x * 2

x = 4

changeValue(x)
print(x)



if __name__ == "__main__":
    main()
