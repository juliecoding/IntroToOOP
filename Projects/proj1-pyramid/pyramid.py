import sys
import time

WEIGHT = 200
cache = {}

function_calls = 0
cache_hits = 0

def calculateWeight(r, c):
    global function_calls
    function_calls += 1
    if (r, c) in cache:
        global cache_hits
        cache_hits += 1
        return cache[(r, c)]

    if r == 0:
        result = 0
    elif c == 0:
        result = (WEIGHT + calculateWeight(r - 1, c)) / 2.0
    elif c == r:
        result = (WEIGHT + calculateWeight(r - 1, c - 1)) / 2.0
    else:
        result = (WEIGHT + calculateWeight(r - 1, c - 1) + calculateWeight(r - 1, c)) / 2.0
    cache[(r, c)] = result
    return result

def main():
    rows = int(sys.argv[1])

    start = time.perf_counter()

    for row in range(rows):
        for col in range(row + 1):
            total = calculateWeight(row, col)
            print(f'{total: .2f}', end = ' ')
        print()

    stop = time.perf_counter()
    print('Elapsed time', stop - start, 'seconds')
    print('Number of function calls:', function_calls)
    print('Number of cache hits:', cache_hits)

main()