# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:56:49 2024

@author: lamngocthaitran
"""

N = int(input("Nhập một số nguyên dương có 2 chữ số: "))

if 10 <= N <= 99:
    hang_chuc = N // 10
    hang_don_vi = N % 10
    tong_chu_so = hang_chuc + hang_don_vi
    print("Tổng các chữ số của", N, "là:", tong_chu_so)
else:
    print("Số bạn nhập không phải là số có 2 chữ số.")