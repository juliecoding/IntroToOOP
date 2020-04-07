import numpy as np

a = np.array(range(10), 'i2') # second argument is datatype

print(a)
print(-a)
print(a + 1)
print(a.dtype, a.itemsize, a.size, a.nbytes, a.shape)

