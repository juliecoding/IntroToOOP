# Python program to show time by perf_counter()
from time import perf_counter
t1_start = perf_counter()

try:
    with open('everyDay.txt', 'r') as readfrom:
        with open('printingToFilePractice.txt', 'w') as f:
            for line in readfrom.readlines():
                print(line.strip(), file = f)
except IOError:
    print('Error reading/writing file')

t1_stop = perf_counter()

# print("Elapsed time:", t1_stop - t1_start)


# Reading numbers from a file (see slide! I didn't write it down)

# formattedOutput
n = 2
x = 10.5
s = 'book'
result = f'{n} {s}s cost ${x*1.06:.2f}'

print(result)