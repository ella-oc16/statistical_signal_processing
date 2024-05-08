import numpy as np

A = np.array([[2, 2, 0], [2, 4, 2], [0, 2, 4]])
A = np.linalg.inv(A)
print(A)
eig = np.linalg.eig(A)
values = np.linalg.eigvals(A)
print(eig)
print(values)