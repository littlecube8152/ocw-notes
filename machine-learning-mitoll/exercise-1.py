import numpy as np

A = np.array([[1, 2],
              [2, 3],
              [3, 4],
              [6, 7]])
B = np.array([[1, 2, 3],
              [2, 3, 4],
              [3, 4, 5],
              [6, 7, 8]])
C = np.array([[1],
              [2],
              [3],
              [4]])
print(C * C)            # point wise multiplication
# print(np.dot(C, C))    
print(np.dot(C.T, C))   
# print(np.dot(A, B))    
print(np.dot(A.T, B))   # actually matrix multiplication 

D = np.array([1, 2, 3])
print(D)

print(A[:,1])           # 1 dimensional array
print(B[:,1:3])         # 2 dimensional array, [a,b)