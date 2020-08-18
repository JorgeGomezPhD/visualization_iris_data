'''Write a Python program to create a 2-D array with ones on the diagonal and zeros elsewhere.
Now convert the NumPy array to a SciPy sparse matrix in CSR format.'''
import numpy as np
from scipy import sparse

eye = np.eye(4)
print("NumPy array:\n", eye)
sparse_matrix = sparse.csr_matrix(eye)
print("\nSciPy sparse CSR matrix:\n", sparse_matrix)