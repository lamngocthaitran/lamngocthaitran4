# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:22:05 2024

@author: hs
"""

gio=int(input("Nhập giờ: "))
phut=int(input("Nhập phút: "))
giay=int(input("Nhập giây: "))
tong_giay = gio * 3600 + phut * 60 + giay 
print("Tong so giay la:", tong_giay)

