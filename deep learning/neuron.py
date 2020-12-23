#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:56:42 2020

@author: ernie
"""

#the basic comutational units in deep neual network

import math

def sigmoid(x):
    y = 1.0 / (1 + math.exp(-x))
    return y
 
def activate(inputs, weights): 
    # perform net input
    h = 0 
    for x,w in zip(inputs, weights):
        h += x*w  # sum up all the inputs which is the net input    
    # perform activation 
    return sigmoid(h)


# the inputs/ the weights/ the calculation in the neuron

inputs  = [0.5, 0.3, 0.2]  # input value for each node
weights = [0.4, 0.7, 0.2]  # weights 
output  =  activate(inputs, weights) # the computation unit of the neuron itself
print(output)
    


