# SHAPE MANIPULATION
## CHANGING THE SHAPE OF AN ARRAY
import numpy as np

a = np.floor(10*np.random.random((3,4)))
print "a => ", a
print "a.shape => ", a.shape

print "\n"

# merubah shape dari array dengan method ravel
print "a.ravel() => ", a.ravel() # flatten the array
a.shape = (6, 2)
print "a.T => ", a.T

print "\n"

# merubah shape dari array dengan method resize
print "a => ", a
a.resize((2,6)) # cara resize array
print "a.resize((2,6)) => ", a

print "\n"

# merubah shape dari array dengan method reshape
# jika diisi -1, dimensinya akan otomatis dikalkulasi
print "a.reshape(3,-1) => ", a.reshape(3,-1)
