## INDEXING WITH ARRAYS OF INDICES
import numpy as np

a = np.arange(12)**2 # 12 bilangan bulat pertama dengan dipangkatkan 2
i = np.array([1,1,3,8,5]) # array dari index
print "a[i] => ", a[i] # elemen dari a pada posisi yang ke i

print "\n"

j = np.array([ [3,4],[9,7] ]) # array bidimensional index
print "a[j] => ", a[j] # bentuk yang sama dari j

print "\n"

palette = np.array([ [0,0,0], # black
                     [255,0,0], # red
                     [0,255,0], # green
                     [0,0,255], # blue
                     [255,255,255] ]) # white

image = np.array([ [0,1,2,0], # tiap nilai sesuai warna dengan pallete
                   [0,3,4,0] ])

print "palette[image] => ", palette[image]

print "\n"

a = np.arange(12).reshape(3,4)
print "a => ", a

print "\n"

i = np.array([ [2,1], # index untuk dim pertama dari a
               [1,2] ])

j = np.array([ [2,1], # index untuk dim kedua
               [3,3] ])

print "a[i,j] => ", a[i,j] # i dan j harus punya shape yang sama

print "\n"

print "a[i,2] => ", a[i,2]

print "\n"

print "a[:,j] => ", a[:,j]

print "\n"

print "a[:,j] => " # sama dengan a[ : ,j]

print "\n"

l = [i,j]
print "a[l] => ", a[l] # sama dengan a[i,j]

s = np.array([i,j])
# a[s] ini tidak dapat dilakukan

print "\n"

print "a[tuple(s)] => ", a[tuple(s)] # same as a[i,j]

time = np.linspace(20, 145, 5)              # time scale
data = np.sin(np.arange(20)).reshape(5,4)   # 4 time dependent series
print "time => ", time

print "\n"

print "data => ", data

print "\n"

ind = data.argmax(axis=0) # index of the maxima for each series
print "ind => ", ind

print "\n"

time_max = time[ind] # times corresponding to the maxima

data_max = data[ind, xrange(data.shape[1])] # => data[ind[0],0], data[ind[1],1]...

print "time_max => ", time_max

print "\n"

print "data_max => ", data_max

print "\n"

print "np.all(data_max == data.max(axis=0)) => ", np.all(data_max == data.max(axis=0))

print "\n"
a = np.arange(5)
print "a => ", a

# kamu dapat juga menggunakan index array untuk menentukkan value
a[[1,3,4]] = 0
print "\n"
print "a => ", a

print "\n"

# akan tetapi ketika list dari index berisi pengulangan, pengisian akan dilakukan berulang kali dan akan menghasilkan nilai yang terakhir
a = np.arange(5)
a[[0,0,2]] = [1,2,3]
print "a => ", a

print "\n"

# hal ini wajar tapi hati-hati dengan menggunakan += karena mungkin tidak sesuai dengan yang diharapkan
a = np.arange(5)
a[[0,0,2]] += 1
print "a => ", a
# meskipun index 0 muncul 2 kali, element 0 hanya di increment sekali

## INDEXING WITH BOOLEAN ARRAYS
a = np.arange(12).reshape(3,4)
b = a > 4 # b ada sebuah boolean with shape a
print "b => ", b

print "\n"

print "a[b] => ", a[b] # id array dengan element yang dipilih

a[b] = 0 # semua element dari a yang lebih dari 4 menjadi 0
print "\n"

print "a => ", a

a = np.arange(12).reshape(3,4)
b1 = np.array([False,True,True]) # first dim selection
b2 = np.array([True,False,True,False]) # second dim selection

print "a[b1,:] => ", a[b1,:] # memilih row yang akan ditampilkan

print "a[b1] => ", a[b1] # sama dengan yang diatas

print "a[:,b2] => ", a[:,b2] # memilih column yang akan ditampilkan

print "a[b1.b2] => ", a[b1,b2] # ??????

print "\n"

## THE ix_() function
# function digunakan untuk menggabungkan vectors yang berbeda sehingga memperoleh hasil untuk setiap n-uplet
a = np.array([2,3,4,5])
b = np.array([8,5,4])
c = np.array([5,4,6,8,3])
ax,bx,cx = np.ix_(a,b,c)
print "ax => ", ax

print "bx => ", bx

print "cx => ", cx

print "\n"

print "shape ax,bx,cx => ", ax.shape, bx.shape, cx.shape

result = ax + bx * cx

print "result => ", result

print "result[3,2,4] => ", result[3,2,4]

print "\n"

print "a[3] + b[2] * c[4] => ", a[3] + b[2] * c[4]

def ufunc_reduce(ufct, *vectors):
    vs = np.ix_(*vectors)
    r = ufct.identity
    for v in vs:
        r = ufct(r,v)
    return r

print "\n"

print ufunc_reduce(np.add,a,b,c)
