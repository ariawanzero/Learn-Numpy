# THE BASIC EXAMPLE
import numpy as np
a = np.arange(15).reshape(3, 5)
print "a = ", a
print "shape = ", a.shape
print "ndim = ", a.ndim
print "dtype.name = ", a.dtype.name
print "itemsize = ", a.itemsize
print "size = ", a.size
print "type = ", type(a)

b = np.array([6, 7, 8])
print "b = ", b
print "type = ", type(b)
