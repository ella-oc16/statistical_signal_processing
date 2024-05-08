import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

"""
NUMPY COLUMN VECTORS
"""
# make a n x 1 matrix, int sets the data type of the vector elements
vector = np.array([[4], [3.3], [5]], int)

# find the magnitude of the vector
norm = np.linalg.norm(vector)
normalised_vector = vector/norm

# time reverse the vector (reverse the order of its elements)
flipped_vector = np.flip(vector)


D = 12
s1 = np.ones((D,1))
s1[int(D/2):D] = -1

norm_s1 = np.linalg.norm(s1)
normalised_s1 = s1/norm_s1
time_reversed_and_normalised_s1 = np.flip(normalised_s1)

h = time_reversed_and_normalised_s1


yn = sp.convolve2d(s1, h)
index2 = np.arange(start=0,stop=yn.shape[0], step=1).reshape(yn.shape)

# Create three subplots
plt.figure(figsize=(6, 9))

# Subplot 1
plt.subplot(3, 1, 1)
index = np.arange(start=0,stop=D, step=1)
index.reshape((s1.shape))
plt.plot(index, s1, marker='o')
plt.title('s1')

# Subplot 2
plt.subplot(3, 1, 2)
plt.plot(index, h, marker='o', color='g')
plt.title('h')

# Subplot 3
plt.subplot(3, 1, 3)
plt.plot(index2, yn, marker='o', color='r')
plt.title('output of convolution')

# Adjust layout for better spacing
plt.tight_layout()
plt.show()

s2 = np.ones((D,1)) 
s2[:int(D/4)] = -1 
s2[3*int(D/4):D] = -1

# Create three subplots
plt.figure(figsize=(6, 9))

# Subplot 1
plt.subplot(3, 1, 1)
index = np.arange(start=0,stop=D, step=1)
index.reshape((s2.shape))
plt.plot(index, s2, marker='o')
plt.title('s2')

# Subplot 2
plt.subplot(3, 1, 2)
plt.plot(index, h, marker='o', color='g')
plt.title('h')

yn = sp.convolve2d(s2, h)
index2 = np.arange(start=0,stop=yn.shape[0], step=1).reshape(yn.shape)

# Subplot 3
plt.subplot(3, 1, 3)
plt.plot(index2, yn, marker='o', color='r')
plt.title('output of convolution')

plt.tight_layout()
plt.show()