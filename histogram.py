import numpy as np
from scipy import linalg as la
import matplotlib.pyplot as plt

print('Enter the size of matrix and number of iterations')
N = int(input())
T = int(input())
eigenvalues = np.array([])
Y = np.arrange(0,T)
for i in  Y:
    a = np.random.randint(0,2,N*N)
    A = 2*a-1
    X = la.eig(A)[0]
    eigenvalues = np.append(eigenvalues,X)
eigenvectors=eigenvalues/(2*(N**(1/2)))
fig, axes = plt.subplots()
bins = np.linspace(-1,1,N+1)
plt.title(' Wigner’s Semicircle Law')
plt.hist(eigenvectors,bins)
plt.grid()
plt.savefig('fig.pdf')
plt.close()