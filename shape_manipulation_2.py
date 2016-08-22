## STACKING TOGETHER DIFFERENT ARRAYS
import numpy as np
a = np.floor(10*np.random.random((2,2)))
print "a => ", a

print "\n"

b = np.floor(10*np.random.random((2,2)))
print "b => ", b

print "\n"

print "np.vstack((a,b)) => ", np.vstack((a,b))
print "np.hstack((a,b)) => ", np.hstack((a,b))

print "\n"

# function column stack 1D colomn ke array mendjadi 2D array, hal ini sama dengan vstack hanya untuk 1D
from numpy import newaxis
print "np.column_stack => ", np.column_stack((a,b)) # dengan 2D arrays

print "\n"

a = np.array([4.,3.])
b = np.array([2.,8.])
print "a[:,newaxis] => ", a[:,newaxis] # ini mengizinkanmu untuk mempunyai 2D columns vector
print "np.column_stack((a[:,newaxis],b[:,newaxis])) => ", np.column_stack((a[:,newaxis],b[:,newaxis]))
print "np.vstack((a[:,newaxis],b[:,newaxis])) => ", np.vstack((a[:,newaxis],b[:,newaxis]))
print "np.r_[1:4,0,4] => ", np.r_[1:4,0,4]
print "np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])] => ", np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])]

print "\n"

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print "np.concatenate((a, b), axis=0) => ", np.concatenate((a, b), axis=0)
print "np.concatenate((a, b.T), axis=1) => ", np.concatenate((a, b.T), axis=1)
