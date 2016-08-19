# Indexing, Slicing and Iterating
# one dimensional array
import numpy as np

a = np.arange(10)**3
print "a = ", a
print "a[2] = ", a[2]
print "a[2:5] = ", a[2:5]

a[:6:3] = -1000 # sama dengan a[0:6:2] = 1000; dari start position sampai posisi ke 6, terutama setiap element ke2 diganti dengan -10000
print "a[:6:2] = -1000 > ", a

print "a [ : :-1] = ", a[ : :-1] # reverse a

for i in a:
    print(i ** (1/3.))

# multidimensional arrays can have one index per axis. These indices are given in a tuple separated by commas:

def f(x,y):
    return 10 * x + y

b = np.fromfunction(f,(5,4),dtype=int)
print "b = ", b
print "b[2,3] = ", b[2,3]
print "b[0:5, 1] = ", b[0:5, 1] # mengambil data pada tiap row, kolom ke dua dari b
print "b[ : , 1] = ", b[ : , 1] # sama dengan contoh sebelumnya
print "b[1:3, : ] = ", b[1:3, : ] # tiap kolom pada baris kedua dan ketiga dari b


print "b[-1] = ", b[-1] # row terakhir sama dengan row index -1

# Ekspresi dalam tanda kurung di b [i] diperlakukan sebagai i diikuti sebanyak dari : yang diperlukan untuk mewakili axes yang tersisa. NumPy juga memungkinkan Anda untuk menulis ini menggunakan titik sebagai b [i, ...].

# Dots (...) mewakili banyak kolom yang dibutuhkan untuk menghasilkan sebuah index tuple yang lengkap
# contoh jika sebuah array mempunyai 5 tingkat maka:
# x[1,2,...] setara dengan x[1,2,:,:,:]
# x[...,3] setara dengan x[:,:,:,:,3] dan
# x[4,...,5,:] setara dengan x[4,:,:,5,:].

c = np.array([[[0, 1, 2],[10, 12, 13]], [[100, 101, 102],[110,112,113]]])
print "shape = ", c.shape
print "c[1,...] = ", c[1,...] # same as c[1,:,:] or c[1]
print "c[...,2] = ", c[...,2] # same as c[:,:,2]

for row in b:
    print(row)

for element in b.flat:
    print (element)
