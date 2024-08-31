# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:54:11 2024

@author: hs
"""

import math
def tinh_chu_vi_ban_kinh_hinh_tron(ban_kinh):
    
    pi= math.pi
    chu_vi=2 *pi *ban_kinh
    dien_tich= pi * ban_kinh * ban_kinh
    
    return chu_vi, dien_tich
if __name__=="__main__":
    ban_kinh=float(input("Nhập bán kính hình tròn: "))
    chu_vi, dien_tich=tinh_chu_vi_ban_kinh_hinh_tron(ban_kinh)
    print("chu vi bán kính hình tròn là: ", chu_vi)
    print("diện tích bán kính hình tròn là: ", dien_tich)
    

    
    
    