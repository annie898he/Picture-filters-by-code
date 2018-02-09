# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 19:47:47 2016

@author: hea
"""

list1=[[2,4,3],\
       [3,5,1],\
       [8,1,6],\
       [4,5,3]]

rows=len(list1)
col=len(list1[0])
temp=[]
whole=[]
for i in range (col):   
    for each in list1:
        if rows == 0:
            rows = len(list1)
            whole.append(temp)
            temp=[]
        num = list1[rows-1][i]
        temp.append(num)
        rows=rows-1
        print rows 
whole.append(temp)
print temp
print whole
