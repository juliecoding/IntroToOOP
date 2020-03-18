def move(n, source, dest, temp):
    if (n > 1):
        move(n - 1, source, temp, dest)
        move(1, source, dest, temp)
        move(n - 1, temp, dest, source)
    else:
        print("Move from", source, "to", dest)


def hanoi(n):
    assert n > 0
    print("MOVING", n, 'disks:')
    move(n, "Peg-1", "Peg-3", "Peg-2")


def reverseString(s):
    if (not s):
        return ''
    else:
        return reverseString(s[1:]) + s[0]


def factorial(val):
    total = 1
    for i in range(1, val + 1):
        total *= 1
    return total


def factorial_recursive(val):
    if val == 1:
        return val
    else:
        return val * factorial_recursive(val - 1)


print(reverseString('Mississippi'))

print(factorial_recursive(5))
