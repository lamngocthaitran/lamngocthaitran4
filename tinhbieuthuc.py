# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:17:23 2024

@author: hs
"""

a=int(input("Nhập a: "))
b=int(input("Nhập b: "))

A=((a+b)/(a**1/3+b**1/3) - (a*b**1/3))/(((a**1/3) - (b**1/3))**2)
print("Kết quả là: ", A)
