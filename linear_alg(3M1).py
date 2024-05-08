import numpy as np

A = np.array([[1, 3], [2, 2], [3, 1]])
U, S, Vh = np.linalg.svd(A)
print(U)
print(S)
print(Vh)

# the pseudoinverse is also called the general