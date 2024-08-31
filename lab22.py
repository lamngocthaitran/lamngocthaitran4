# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:28:56 2024

@author: ADMIN
"""

print("giải phương trình bậc nhất")
a = float(input("Nhập a:"))
b = float(input("Nhập b:"))
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print("Nghiệm của phương trình là: ", x)