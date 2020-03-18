import Module1ClassCode as mcc
# val = mcc.square(8)
# print(val)
# print(mcc.addListRecursively([1, 2, 3, 4, 5]))


def fib(n):
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


112358
print(fib(5))

cache = {}


def recursive_fib_with_cache(n):
    if n in (0, 1):
        result = n
    elif n in cache:
        result = cache(n)
        print('fib(', n, ') found in cache')')
    else
        result=fib(n - 1) + fib(n - 2)
        cache[n]=result
    return result

def iterative_fib(n):
    if n in (0, 1)
        return n
    first, second=1, 1
