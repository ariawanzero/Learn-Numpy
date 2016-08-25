## Simple Array Operations
import numpy as np

a = np.array([ [1.0, 2.0], [3.0,4.0] ])
print "a => ", a

print "\n"

print "transpose => ", a.transpose()

print "\n"

print np.linalg.inv(a)

print "\n"

u = np.eye(2) # unit 2x2 matrix; "eye" represents "I"
print "np.eye(2) => ", u

j = np.array([ [0.0, -1.0], [1.0, 0.0] ])
print "\n"

print np.dot(j, j) # matrix product

print "\n"

print np.trace(u) # trace

print "\n"

y = np.array([ [5.], [7.] ])
print np.linalg.solve(a, y)

print "\n"

print np.linalg.eig(j)

