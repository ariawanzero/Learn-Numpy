## NO COPY AT ALL
import numpy as np

a = np.arange(12)
b = a # tidak ada object baru yang dibuat
print "b is a => ", b is a # a dan b adalah 2 variable untuk object ndarray yang sama

b.shape = 3,4
print "a.shape => ", a.shape

print "\n"

def f(x):
    print(id(x))

print "id(a) => ", id(a)
print "f(a) => ", f(a)

print "\n"

## VIEW OR SHALLOW COPY
c = a.view()
print "c is a => ", c is a
print "c.base is a => ", c.base is a # c adalah sebuah view dari data yang dipunyai oleh variable a
print "c.flags.owndata => ", c.flags.owndata

print "\n"

c.shape = 2,6
print "a.shape => ", a.shape
c[0,4] = 1234
print "a => ", a

print "\n"

# slicing an array returns a view of it
s = a[ : , 1:3] # spaces added for clarity: could also be written "s = a[:,1:3]"
s[:] = 10 # s[:] is a view of s. Note the difference between s=10 and s[:]=10
print "a => ", a

print "\n"
## DEEP COPY
d = a.copy() # sebuah object array baru dengan data yang baru dibuat
print "d is a => ", d is a
print "d.base is a => ", d.base is a # tidak membagi apapun dengan variable a
d[0,0] = 9999
print "a => ", a




