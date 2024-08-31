# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:38:27 2024

@author: ADMIN
"""

chucai = input("Nhập một chữ cái: ")
def doi_hoa_thuong(chucai):
  if chucai.islower():
    return chucai.upper()
  elif chucai.isupper():
    return chucai.lower()
  else:
    return "Không phải chữ cái"
ket_qua = doi_hoa_thuong(chucai) 
print("Chữ cái sau khi đổi:", ket_qua)
    

