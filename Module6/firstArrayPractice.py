import numpy as np
import matplotlib.pyplot as plt

a = np.array(range(10), 'i2') # second argument is datatype

print(a)
print(-a)
print(a + 1)
print(a.dtype, a.itemsize, a.size, a.nbytes, a.shape)

# plt.plot([1, 2, 3, 4, 5])
# plt.xlabel("x label")
# plt.ylabel("y label")
# plt.show()

# _,axis = plt.subplots()
# axis.plot([10, 29, 31, 9, 35, 17, 5])
# axis.set(title="A simple line plot of y values")
# plt.show()

x0 = np.linspace(.25, .5, 8)[:-1]
x1 = np.linspace(.5, 1.0, 8)[:-1]
x2 = np.linspace(1.0, 2.0, 8)[:-1]
x3 = np.linspace(2.0, 4.0, 8)[:-1]
x4 = np.linspace(4.0, 8.0, 8)[:-1]
x5 = np.linspace(8.0, 16.0, 8)[:-1]
x6 = np.linspace(16.0, 32.0, 8)[:-1]
x7 = np.linspace(32.0, 64.0, 8)[:-1]

x = np.concatenate((x0, x1, x2, x3, x4, x5, x6, x7))
y = np.zeros(len(x))

_,ax = plt.subplots()
ax.plot(x, y, marker = "|")
plt.show()