#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:37:02 2021

@author: ernie
"""

class XuLie:
    
    def __init__(self, property1, property2, property3):
        self.classProperty1 = property1
        self.classProperty2 = property2
        self.classProperty3 = property3    
        



xuLieInstance = XuLie('passed string', 123, 'another string')



print(xuLieInstance.classProperty1)