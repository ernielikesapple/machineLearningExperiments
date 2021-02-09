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
        
        print("one class has been initiated, first property is: ", property1)
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
        
    
    

class DianLiGongYingXuLie(XuLie):
    specialChildProperty = "this property is unique from the parent class"
    
    def __init__(self, property1, property2, property3, addtionalChildPropery1):
        super().__init__(property1, property2, property3)
        #XuLie.__init__(self, property1, property2, property3)   # another way to init from the parent class
        self.addtionalChildPropery1 = addtionalChildPropery1 #this property is unique from the parent class
        


class ZhenKongXuLie(XuLie):
    specialChildProperty = "this property is unique from the parent class"
    
    def __init__(self, property1, property2, property3, buzhouLists=None):
        super().__init__(property1, property2, property3)
        #XuLie.__init__(self, property1, property2, property3)   # another way to init from the parent class
        if buzhouLists is None:  # never pass mutable data types like lists or dictionary as default arguments
            self.buzhouLists = []  
        else:
            print("add buzhou into lists")
            self.buzhouLists = buzhouLists
        
    def add_Buzhou(self, buzhou):
        if buzhou not in self.buzhouLists:
            self.buzhouLists.append(buzhou)
    
    def remove_Buzhou(self, buzhou):
        if buzhou in self.buzhouLists:
            self.buzhouLists.remove(buzhou)    
    
    def print_buZhou(self):
        for buzhou in self.buzhouLists:
            print(" 打印所有buzhou-->", buzhou.mingzi)
        


class Buzhou:
    
    def __init__(self, mingzi, miaoshu):
        self.mingzi = mingzi
        self.miaoshu = miaoshu
        
        


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


dianLiGongYingXuLie = DianLiGongYingXuLie('this is an inherited class', 123, 'another string', "this property is unique from the parent class")

print("we have sum up : ", XuLie.classCounter, "classes instance have been instantiated")
print("child has a unique property ", dianLiGongYingXuLie.addtionalChildPropery1, " and it has all the parent property:", dianLiGongYingXuLie.classProperty1)



buzhou1 = Buzhou("this is a buzhou", "test")
buzhou2 = Buzhou("this is a buzhou2", "test")
zhenkongXuLieCeShi = ZhenKongXuLie("123", "123", "123", [buzhou1])

zhenkongXuLieCeShi.add_Buzhou(buzhou2)
zhenkongXuLieCeShi.remove_Buzhou(buzhou1)

zhenkongXuLieCeShi.print_buZhou()

print(help(ZhenKongXuLie))  #check inheritance, in the "Method resolution order:" section
print(issubclass(ZhenKongXuLie, XuLie))
print(isinstance(zhenkongXuLieCeShi, XuLie))




