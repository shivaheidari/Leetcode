import numpy as np


def matrix_mul (a,b):
    return a @ b

def transpose(a):
    return a.T

def invert(a):
    return np.linalg.inv(a)


def eigenvalues(a):
 eigenvalue, eigenvector = np.linalg.eigh(a)
 return eigenvalue, eigenvector

a = np.random.rand(3,3)
b = np.random.rand(3,3)
print(matrix_mul(a,b))
print(transpose(a))
print(invert(a))
print(eigenvalues(a))

