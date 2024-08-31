# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:08:17 2024

@author: ADMIN
"""

ngay = input("Nhập ngày sinh: ")
thang = input("Nhập tháng sinh: ")
nam = input("Nhập năm sinh: ")
a=f"{ngay}/{thang}/{nam}"
print(a)
b = f"{ngay}/{thang}/{str(nam)[-2:]}"
print(b)
c = f"{nam}/{thang}/{ngay}"
print(c)
nhap_a = input("Nhập ngày/tháng/năm: ")
ngay_a, thang_a, nam_a = map(int, nhap_a.split('/'))

nhap_b = input("Nhập ngày/tháng/năm (năm rút gọn): ")
ngay_b, thang_b, nam_b = map(int, nhap_b.split('/'))
nam_b += 1900 if nam_b >= 50 else 2000

nhap_c = input("Nhập năm/tháng/ngày: ")
nam_c, thang_c, ngay_c = map(int, nhap_c.split('/'))
print("Ngày/tháng/năm từ định dạng a): ", ngay_a, thang_a, nam_a)
print("Ngày/tháng/năm từ định dạng b): ", ngay_b, thang_b, nam_b)
print("Ngày/tháng/năm từ định dạng c): ", ngay_c, thang_c, nam_c)



