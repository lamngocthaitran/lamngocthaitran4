# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 08:47:23 2024

@author: ADMIN
"""

a=int(input("nhap gio thu 1: "))
b=int(input("nhap phut thu 1: "))
c=int(input("nhap giay thu 1: "))
d=int(input("nhap gio thu 2: "))
e=int(input("nhap phut thu 2: "))
f=int(input("nhap giay thu 2: "))
thu1=a*3600+b*60+c
thu2=d*3600+e*60+f
print("kêt quả công 2 gờ: ",int((thu1+thu2)),"giay")
print("kêt quả trừ 2 gờ: ",int((thu1-thu2)),"giay")
print(f"{a+d}giờ{b+e}phút{c+f}giây")
print(f"{a-d}giờ{b-e}phút{c-f}giây")
