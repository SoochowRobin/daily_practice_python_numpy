# this python file is used to calcualte variance, covariance by using numpy
import numpy as np

# the arithmetic mean could be calcualted by using numpy method mean()
v = np.array([1, 2, 3, 4, 5, 6])
mean = np.mean(v) # mean() method in numpy
print(mean)

# calculate mean of matrix by using mean(axis=0 --> col,  axis=1 --> row)
M = np.array([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]])
col_mean = np.mean(M, axis=0) # axis=1 ---> row
row_mean = np.mean(M, axis=1) # axis=0 ---> col
print(col_mean)
print(row_mean)

# in numpy, the variance of vector and matrix are calculated by using Var() method
t = np.array([1,2,3,4,5,6])
variance = np.var(t, ddof=1)  # calculate the variance of vector, ddof should set to 1
print(f'variance of this vector is that {variance}')

# calculate the variance of matrix
t_d = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
row_variance = np.var(t_d, axis=1, ddof=1)
col_variance = np.var(t_d, axis=0, ddof=1)
print(f'row variance is that {row_variance}')
print(f'col_variance is that {col_variance}')

# calculate the standard deviation of the matrix, the std() is the square root of variance
row_std = np.std(t_d, ddof=1, axis=1)
col_std = np.std(t_d, ddof=1, axis=0)
print(f'row std is {row_std}')
print(f'col_std is {col_std}')
