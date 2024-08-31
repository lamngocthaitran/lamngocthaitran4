# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:08:35 2024

@author: hs
"""

def chu_hoa(chu_thuong):
    return chu_thuong.upper()
ky_tu_thuong = input("Nhập một ký tự chữ thường: ")
ket_qua=chu_hoa(ky_tu_thuong)
print("ký tự hoa tương ứng là: ", ket_qua)

