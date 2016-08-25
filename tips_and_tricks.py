## Automatic Reshaping
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(30)
a.shape = 2,-1,3 # -1 berarti terserah berapapun yang dibutuhkan

print a.shape
print "\n"
print a

## Vector Stacking
x = np.arange(0,10,2) # x = ([0,2,4,6,8])
y = np.arange(5) # y = ([0,1,2,3,4,])
m = np.vstack([x,y]) # m = ([[0,2,4,6,8],
                     #       [0,1,2,3,4]])
xy = np.hstack([x,y]) # xy = ([0,2,4,6,8,0,1,2,3,4])

## Histogram
# Build a vector of 10000 normal deviates with variance 0.5^2 dan mean 2
mu, sigma = 2, 0.5
v = np.random.normal(mu,sigma,10000)

# PLot a normalized histogram with 50 bins
plt.hist(v, bins=50, normed=1) # matplotlib version (plot)
plt.show()

# Compute the histogram with numpy an the plot it
(n, bins) = np.histogram(v, bins=50, normed=True) # NumPy version (no plot)
plt.plot(.5 * (bins[1:]+bins[:-1]), n)
plt.show()

