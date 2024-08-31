# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:52:39 2024

@author: hs
"""

a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))
d=int(input("Nhập số d: "))
so_nho_nhat = a
if b < so_nho_nhat:
   so_nho_nhat=b
if c < so_nho_nhat:
   so_nho_nhat=c
if d < so_nho_nhat:
   so_nho_nhat=d
print("kết quả là: ", so_nho_nhat)
    