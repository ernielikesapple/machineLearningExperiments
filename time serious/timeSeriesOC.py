#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 10:57:38 2021

@author: ernie
"""

# # Filling in the gaps in a timeseries via linear interpolation.
# # -------------------------------------------------------------
# 
# # Let's say we have an array of points like this, that we're plotting on a graph:
# # timeseries = [
# #   { x: 1, y: 1.25 },
# #   { x: 5, y: 2.25 },
# #   { x: 10, y: 1 },
# #   { x: 20, y: 2.12 }
# # ]
# # 
# #
# # What we really want is to have one point on our graph for each integer X value. Notice that we don't have a coordinate where x is 2, 3, 4, 6, 7, 8, 9, etc. Let's fill in these coordinates, and set the corresponding Y values to be such that we generate straight lines between the points we know.
# #
# # expected_output = [
# #   { x: 1, y: 1.25 }, <-- same as input
# #   { x: 2, y: 1.5 },
# #   { x: 3, y: 1.75 },
# #   { x: 4, y: 2 },
# #   { x: 5, y: 2.25 }, <-- same as input
# #   { x: 6, y: 2 },
# #   { x: 7, y: 1.75 },
# #   { x: 8, y: 1.5 },
# #   { x: 9, y: 1.25 },
# #   { x: 10, y: 1 }, <-- same as input
# #   .
# #   .
# #   .
# # ]
# 
# # Overall: Write a method that accepts a timeseries and outputs a new array (ie. so not done in-place) with the gaps filled in.



timeseries = [ { 'x': 1, 'y': 1.25 }, { 'x': 5, 'y': 2.25 }, { 'x': 10, 'y': 1 }, { 'x': 20, 'y': 2.12 }]


#print(f'Songs --> {songs} \n')
#title = list(map(lambda x : x['title'], songs))
#print(f'Print Title --> {title}')



def outPutNewArray(ts): 
    previous = next_ = None
    lengthOfTs = len(ts)
    for index, obj in enumerate(ts):
        print('index is: ', index)
        print('obj is ', obj)
       
        if index > 0:
            previous = ts[index - 1]
            print('previous is ', previous)
        if index < (lengthOfTs - 1):
            next_ = ts[index + 1]
            print('next item is', next_)
           
outPutNewArray(timeseries)

