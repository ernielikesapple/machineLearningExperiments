#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:38:35 2020

@author: ernie
"""

from itertools import islice

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multivariate_normal
from functools import reduce


# multivariate_normal
# x, y = np.mgrid[-1.0:1.0:30j, -1.0:1.0:30j]
# var = multivariate_normal(mean=[0,0], cov=[[1,0],[0,1]])  # z value 
# z = var.pdf([1,0])
# # z = z.reshape(x.shape)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(x,y,var)
# plt.show()

filename = 'Assignment3_dataset.txt'
lines = []

# initialize data
with open(filename, "r") as lines:
    dataw1 = np.genfromtxt(islice(lines, 1, 11))

# with open(filename, "r") as lines:
#     dataw1_missing = np.genfromtxt(islice(lines, 1, 11))

with open(filename, "r") as lines:
    dataw2 = np.genfromtxt(islice(lines, 12, 22))

with open(filename, "r") as lines:
    dataw3 = np.genfromtxt(islice(lines, 23, 33))    




completeDataW1 = dataw1[:,:2]
W1_third_column_with_missing_Data = dataw1[:,2]

W1_third_column_with_missing_Data[::2] = np.nan

print('completeDataW1: \n' , np.matrix(completeDataW1))
print('restDataMeanW1:' , W1_third_column_with_missing_Data)

# a = W1_third_column_with_missing_Data.reshape(10,1) 
# print("size" , a.shape)

processedData = np.append(completeDataW1, W1_third_column_with_missing_Data.reshape(10,1), axis=1)   # reshape!!! to make 1d array to matrix!! notice before reshape the size is (10,), after reshape it's (10,1)

miu0 = np.matrix([[0,0,0]])
print(miu0)
sigma0 = np.identity(3)
print(sigma0)

# def EMalgorithm(data, mu0, sigma0, iterationTimes):
#     miu_iPlus1 = mu0
#     sigma_iPlus1 = sigma0    
#     sum1 = 0
#     for d in data:
#         sum1 += d    
#     print('本次', sum1/10)
# EMalgorithm(processedData, miu0,sigma0, 1)        

 https://joon3216.github.io/research_materials/2019/em_imputation.html

def impute_em(X, max_iter = 3000, eps = 1e-08):
    '''(np.array, int, number) -> {str: np.array or int}
    
    Precondition: max_iter >= 1 and eps > 0
    
    Return the dictionary with five keys where:
    - Key 'mu' stores the mean estimate of the imputed data.
    - Key 'Sigma' stores the variance estimate of the imputed data.
    - Key 'X_imputed' stores the imputed data that is mutated from X using 
      the EM algorithm.
    - Key 'C' stores the np.array that specifies the original missing entries
      of X.
    - Key 'iteration' stores the number of iteration used to compute
      'X_imputed' based on max_iter and eps specified.
    '''
    
    nr, nc = X.shape
    C = np.isnan(X) == False
    
    # Collect M_i and O_i's
    one_to_nc = np.arange(1, nc + 1, step = 1)
    M = one_to_nc * (C == False) - 1
    O = one_to_nc * C - 1
    
    # Generate Mu_0 and Sigma_0
    Mu = np.nanmean(X, axis = 0)
    observed_rows = np.where(np.isnan(sum(X.T)) == False)[0]
    S = np.cov(X[observed_rows, ].T)
    if np.isnan(S).any():
        S = np.diag(np.nanvar(X, axis = 0))
    
    # Start updating
    Mu_tilde, S_tilde = {}, {}
    X_tilde = X.copy()
    no_conv = True
    iteration = 0
    while no_conv and iteration < max_iter:
        for i in range(nr):
            S_tilde[i] = np.zeros(nc ** 2).reshape(nc, nc)
            if set(O[i, ]) != set(one_to_nc - 1): # missing component exists
                M_i, O_i = M[i, ][M[i, ] != -1], O[i, ][O[i, ] != -1]
                S_MM = S[np.ix_(M_i, M_i)]
                S_MO = S[np.ix_(M_i, O_i)]
                S_OM = S_MO.T
                S_OO = S[np.ix_(O_i, O_i)]
                Mu_tilde[i] = Mu[np.ix_(M_i)] + S_MO @ np.linalg.inv(S_OO) @(X_tilde[i, O_i] - Mu[np.ix_(O_i)])
                X_tilde[i, M_i] = Mu_tilde[i]
                S_MM_O = S_MM - S_MO @ np.linalg.inv(S_OO) @ S_OM
                S_tilde[i][np.ix_(M_i, M_i)] = S_MM_O
        Mu_new = np.mean(X_tilde, axis = 0)
        S_new = np.cov(X_tilde.T, bias = 1) + reduce(np.add, S_tilde.values()) / nr
        no_conv = np.linalg.norm(Mu - Mu_new) >= eps or np.linalg.norm(S - S_new, ord = 2) >= eps
        Mu = Mu_new
        S = S_new
        iteration += 1
    
    result = {
        'mu': Mu,
        'Sigma': S,
        'X_imputed': X_tilde,
        'C': C,
        'iteration': iteration
    }
    
    return result



result_imputed = impute_em(processedData)

print("mean is: \n", result_imputed['mu'])


print("Sigma is: \n", result_imputed['Sigma'])


