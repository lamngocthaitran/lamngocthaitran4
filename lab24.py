# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:22:24 2024

@author: ADMIN
"""

gio=int(input("nhập giờ: "))
phut=int(input("nhập phút: "))
giay=int(input("nhập giây: "))

def kiemtrathoigian(gio,phut,giay):
    if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
     return True
    else:
     return False
if kiemtrathoigian(gio,phut,giay):
     print("thời gian hợp lệ")
     
else:
    print("thời gian không hợp lệ")
    
         