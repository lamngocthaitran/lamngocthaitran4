# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:29:41 2024

@author: hs
"""

a=float(input("Nhập số a:"))
b=float(input("Nhập số b:"))
c=float(input("Nhập số c:"))
D=b*b-4*a*c
if D==0:
    print("Phương trình có nghiệm kép x1 = x2 =",-b/(2*a))
if D>0:
    print("Phương trình có hai nghiệm x1=",(-b+D**0.5)/(2*a),"và x2=",(-b-D**0.5)/(2*a))
if D<0:
    print("Phương trình vô nghiệm")