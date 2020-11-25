#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 20:59:59 2020

@author: ernie
"""

#kmeans algorithm: https://www.youtube.com/watch?v=4b5d3muPQmA&list=PLlcyUWQOcKAgDvemP5qJp0kcvWU5n-d7V&index=1

#code for this file : https://www.youtube.com/watch?v=v-SjKuFZV7A

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split # split our data into training and testing part 
from sklearn import metrics # to evalutate performance of algorithms

iris = datasets.load_iris()  # original iris data



X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)

# print('test data is \n' ,X_test)
# print('each test data is belong to class x: \n' ,y_test)

# X_train is the train data, X_test is going to varify the model later
# y_train is the for each train data, which class it belongs to, so does y_test

model = KMeans(n_clusters=3)
# model.fit(X_train, y_train)
model.fit(X_train)  # todo: question both of the line above above is ok?

print(model.score) # todo: meaning??

# print(X_train ,'\n')
# print(y_train ,'\n')

# plt.show()  # todo: it's 4 d data, need to find ways to plot it
accuracy_kmeans = metrics.accuracy_score(y_test, model.predict(X_test))
print('accuracy_kmeans', accuracy_kmeans)

from sklearn.mixture import GaussianMixture
model_gmm = GaussianMixture(n_components=3)  # assume there are 3 gaussian clusters

model_gmm.fit(X_train)

accuracy_gmm = metrics.accuracy_score(y_test, model_gmm.predict(X_test))

print('accuracy_gmm', accuracy_gmm)