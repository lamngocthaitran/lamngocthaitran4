# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:04:00 2024

@author: lamngocthaitran
"""

gio=int(input("Nhập giờ: "))
phut=int(input("Nhập phút: "))
giay=int(input("Nhập giây: "))
tong_giay = gio * 3600 + phut * 60 + giay 
print("Tong so giay la:", tong_giay)