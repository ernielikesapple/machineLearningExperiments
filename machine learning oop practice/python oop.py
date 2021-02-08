#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:37:02 2021

@author: ernie
"""

class XuLie:
    
    classPropertiesName = "default name"
    
    classCounter = 0  
    
    def __init__(self, property1, property2, property3):
        self.classProperty1 = property1               # this is a instance variable, when calling like Class.property, it won't show
        self.classProperty2 = property2
        self.classProperty3 = property3  
        
        XuLie.classCounter += 1  # by calling like  Class.property directly, this property will keep increasing when instantiating a new class instance
        
    def thisIsAFunction(self):
        return '{} + {}'.format(self.classProperty1, self.classProperty2)

    def printClassName(self):
        return print("print self.classPropertiesName", self.classPropertiesName, "  ","print Class.classPropertiesName", XuLie.classPropertiesName)
    
    @classmethod         # another way to create the class
    def alternativeClassInstructor(cls, p1):
        property1, property2, property3 = p1.split('@')
        return cls(property1, property2, property3)
    
    
    @staticmethod   # has a logical connection but it doesn't depond on any class or instance variables
    def thisIsAstaticMethod(FirstParameterDontNeedToBeClassOrInstance):
        return print(FirstParameterDontNeedToBeClassOrInstance, "if you are not accessing the class or instance anywhere in the function")
        

xuLieInstance = XuLie('passed string', 123, 'another string')

print(xuLieInstance.classProperty1)
print(xuLieInstance.thisIsAFunction())

'''
XuLie.thisIsAFunction(xuLieInstance)
# is the same with the line 
xuLieInstance.thisIsAFunction() # this pass xuLieInstance to the function directly
'''

XuLie.classPropertiesName = "new name" 
xuLieInstance.classPropertiesName = "new name"  #notice the class instance is not affected inside printClassName method!
XuLie.printClassName(xuLieInstance)

xuLieInstance2 = XuLie('passed string', 123, 'another string')
print("we have sum up : ", XuLie.classCounter, "classes instance have been instantiated")

newXuLieInstance = XuLie.alternativeClassInstructor("sad@aaa@bbb")
print("we have sum up : ", XuLie.classCounter, "classes instance have been instantiated")

newXuLieInstance.thisIsAstaticMethod("static method is like: ")