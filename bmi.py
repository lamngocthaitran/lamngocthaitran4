# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:21:45 2024

@author: hs
"""

def tinh_bmi(cannang, chieucao):
    bmi=cannang/(chieucao**2)
    return bmi
if __name__=="__main__":
    chieucao=float(input("Nhập chiều cao của bạn m: "))
    cannang=float(input("NHập cân cặng của bạn kg: "))
    bmi=tinh_bmi(cannang, chieucao)
    print("kết quả là: ", bmi)
    

    
        
        