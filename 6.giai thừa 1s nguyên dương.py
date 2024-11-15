# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 22:13:44 2024

@author: Vivobook
Viết một hàm để tính giai thừa của số nguyên dương n . Giai thừa của n (ký hiệu là n! ) là
tích của tất cả các số từ 1 đến n .
Chữ ký hàm
Đầu vào
Đầu ra
Ví dụ
Ví dụ 1:
Giải thích: 5! = 5 × 4 × 3 × 2 × 1 = 120.
Ví dụ 2:
Giải thích: 7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040.

"""
def question_6(n: int) -> int:
    if n<0:
        return False
    tong=1
    for i in range(1,n+1):
        tong*=1
    return tong














def question_6(n: int) -> int:
    if n<=0:
        return False
    tong=1
    for i in range(1, n+1):
        tong*=i
    return tong
if __name__=="__main__":
    n=int(input("Nhập n: "))
    print(question_6(n))\
        


def question_6(n: int) -> int:
    if

