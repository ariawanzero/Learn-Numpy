## BASIC OPERATIONS
import numpy as np
from numpy import pi

a = np.array( [20,30,40,50] )
b = np.arange( 4 )
print "b = ", b

c = a - b
print "a - b = ", c

b**2
print "b**2 = ", b

print "10 * np.sin(a) = ",10 * np.sin(a)

print "a = ",a < 35

A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])

print "A * B >> ", A * B

# perkalian dot matriks
print "A dot B >> ", A.dot(B)

print "np.dot(A, B) >> ", np.dot(A, B)

# some operation such as += and *= bertujuan untuk memodifikasi array daripada membuat yang baru
a = np.ones((2, 3), dtype=int)
b = np.random.random((2,3))
a *= 3
print "a *= 3 >> ", a
b += a
print "b += a >> ", b
a += b
print "a += b", a # hal ini tidak menghasilkan apapun karena perbedaan tipe data a & b

a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)
print "b.dtype.name >> ", b.dtype.name

c = a + b
print "c = a+b >> ",c
print "c.dtype.name >> ", c.dtype.name

d = np.exp(c * 1j)
print "d = np.exp(c * 1j) >> ", d
print "d.dtype.name >> ", d.dtype.name

a = np.random.random((2,3))
print a
print "a.sum() >> ", a.sum()
print "a.min() >> ", a.min()
print "a.max() >> ", a.max()

# axis menentukkan apakah operasi function berdasarkan row atau column
b = np.arange(12).reshape(3,4)
print b
print "b.sum(axis=0) >> ", b.sum(axis=0) # sum tiap column
print "b.min(axis=1) >> ", b.min(axis=1) # min dari row
print "b.cumsum(axis=1) >> ", b.cumsum(axis=1) # cumulative sum sepanjang row
