# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:33:44 2024

@author: hs
"""

a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))
d=int(input("Nhập số d: "))
so_lon_nhat = a
if b > so_lon_nhat:
   so_lon_nhat=b
if c > so_lon_nhat:
   so_lon_nhat=c
if d > so_lon_nhat:
   so_lon_nhat=d
print("kết quả là: ", so_lon_nhat)