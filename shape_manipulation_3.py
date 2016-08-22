## SPLITTING ONE ARRAY INTO SEVERAL SMALLER ONES
import numpy as np
a = np.floor(10*np.random.random((2,12)))
print "a => ", a
print "np.hsplit(a,3) => ", np.hsplit(a,3) # split menjadi 3 array
print "np.hsplit(a,(3,4)) => ", np.hsplit(a,(3,4)) # split a setelah kolom ke3 dan kolom ke4

print "\n"

x = np.arange(16.0).reshape(4,4)
print "x => ", x
print "np.vsplit(x,2) => ", np.vsplit(x,2)
print "np.vsplit(x,(3,4)) => ", np.vsplit(x,(3,4))

print "\n"

x = np.arange(8.0).reshape(2,2,2)
print "x => ", x
print "x.vspilt(x, 2) => ", np.vsplit(x, 2)


print "\n"

print "np.array_split(x, 3) => ", np.array_split(x, 3)

