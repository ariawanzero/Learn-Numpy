import numpy as np
from numpy import pi
print 'Using linspace = ', np.linspace(0, 2, 9)

x = np.linspace(0, 2*pi, 100)
print "x = ", x

f = np.sin(x)
print "f = ", f

## PRINTING ARRAYS
a = np.arange(6)
print "a = ", a

b = np.arange(12).reshape(4, 3)
print "b = ", b

c = np.arange(24).reshape(2, 3, 4)
print "c = ", c

print "arange = ", (np.arange(10000))

print "arange with shape = ", (np.arange(10000)).reshape(100,100)

print np.set_printoptions(threshold='nan') # ini untuk menampilkan semua list tanpa disingkat

print "arange = ", (np.arange(10000))

print "arange with shape = ", (np.arange(10000)).reshape(100,100)


