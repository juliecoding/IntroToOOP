import math

TOLERANCE = 0.000001


def newton(x):
    estimate = 1.0
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= TOLERANCE:
            break
    return estimate


def newtonRecursive(x, estimate=1.0):
    difference = abs(x - estimate ** 2)
    if difference <= TOLERANCE:
        return estimate
    else:
        estimate = (estimate + x / estimate) / 2
        return newtonHelper(x, estimate)
