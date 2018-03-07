# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 15:04:26 2018

@author: PC
"""

def fab(m):
    a,b=1,1
    while a<m:
        yield a
        a,b=b,a+b
c=fab(5)
print [o for o in c] 
