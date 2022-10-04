import numpy as np

M = np.array([[2,3],[5,4]])
y = np.array([2,3])

# @ means Matrix Multiplication 
M_sq = M.T @ M
#print(X_sq)
M_inv = np.linalg.inv(M_sq)
beta_hat = M_inv @ (M.T @ y)
print(beta_hat)