#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:28:31 2020

@author: ernie
"""
"""
Spyder Editor

This is a temporary script file.
"""
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np;

'''
w1X = [0, 0, 2, 3, 3, 3];
w1Y = [0, 1, 2, 1, 2, 3];
w1Actual = np.stack((w1X, w1Y), axis=-1)
print(w1Actual)
covMatrix_w1Actual = np.cov(w1Actual)
print(covMatrix_w1Actual)
w2 = [];
# mean1Forw1X  = np.mean(w1X, w1Y);
print(mean1Forw1X)
mean1Forw1Y  = np.mean(w1Y);
print(mean1Forw1Y)
covMatrix = np.cov(w1X, w1Y)  
print(covMatrix)
'''


'''  
#version 2 after see the stack overflow


# calculate the column mean https://stackoverflow.com/questions/15819980/calculate-mean-across-dimension-in-a-2d-array
# calculate the column covariance https://stackoverflow.com/questions/15036205/numpy-covariance-matrix


w1 = np.array([[0,0], [0,1], [2,2], [3,1], [3,2], [3,3]]);
print(w1[:,1])  #only extract the second column of the array!!!. remember define the array as an numpy array!!! 
print(w1.mean(axis=0)) # calculate the mean in each column, if axis =1, then it's the mean for each row!!
print(np.cov(w1[:,0],w1[:,1]))   #notice if we don't specify the bias variable, the denominator is n-1, using the sample covariance
'''



# manually caculate the co-variance
w1 = np.array([[0,0], [1,1], [2,2], [3,2], [4,2], [5,3]]);
w2 = np.array([[6,9],[8,10],[9,10],[9,11], [10,10], [11,12], [12,12], [12,13]])

def printMeanNCov (para):           # step by step to calculate the mean and covariance in a two dimensional numpy array
    deviation = para - para.mean(axis=0)
    deviationT = deviation.transpose()
    dotProduct = np.dot(deviationT, deviation)
    covW = dotProduct / (len(para) - 1)    # sample mean
    print('mean is \n',  para.mean(axis=0))
    print('covW is \n', covW)

printMeanNCov(w1)
printMeanNCov(w2)


# quick way to do it, 
print('covairance is \n', np.cov(w1[:,0] ,w1[:,1]))  # answer 
print('covairance is \n', (np.cov(w2[:,0] ,w2[:,1], bias =True)) * 9 / 8) 




