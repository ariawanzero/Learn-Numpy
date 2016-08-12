## ARRAY CREATION EXAMPLE
import numpy as np
a = np.array([1,2,3,4])
print "a = ", a
print "dtype = ", a.dtype

b = np.array([1.2, 3.5, 5.2])
print "b = ", b
print "dtype = ", b.dtype

# can't use make array like this np.array([1, 2, 3])

# array transform into 2-dimensional array, persequences into three dimensional arrays and so on
c = np.array([(1.5,2,3), (4,5,6), (2,3,4,2)])
print "c = ", c

# tipe dari array dapat juga secara explisit ditentukan oleh waktu penciptaan
d = np.array( [ [1,2], [3,4] ], dtype=complex )
print "d = ", d

# function ini membuat array menjadi full of 0
print np.zeros( (3,4) )

# function ini membuat array menjadi full of 1
print np.ones( (2,3,4), dtype=np.int16 ) # dtype can also be specified

# function ini membuat content array adalah random dan tergantung pada keadaan memori
print np.empty( (2,3) ) # unintialized, output may vary

# membuat urutan nomer. Numpy menyediakan fungsi analogy range yang mengembalikan dalam bentuk array bukan list
print np.arange(10, 30, 5)

print np.arange(0, 2, 0.3) # function ini menerima decimal

