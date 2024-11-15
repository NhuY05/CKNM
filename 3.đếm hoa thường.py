# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 23:54:01 2024

@author: Vivobook
Viết một hàm nhận vào một chuỗi, sau đó đếm và in ra số lượng ký tự viết hoa và ký tự viết
thường trong chuỗi đó.
Chữ ký hàm
Đầu vào
Đầu ra
Ví dụ
Ví dụ 1:
Một chuỗi ký tự s .
Trả về 2 giá trị:
1. Số lượng ký tự viết hoa trong chuỗi.
2. Số lượng ký tự viết thường trong chuỗi.
"""

def question_3(s: str) -> (int, int):
    kituhoa=0
    kituthuong=0
    for i in s:
        if i.isupper():
            kituhoa+=1
        elif i.islower():
            kituthuong+=1
    return kituhoa, kituthuong
if __name__=="__main__":
    print(question_3("NHUnhuy"))



def question_3(s: str) -> (int, int):
    kituhoa=0
    kituthuong=0
    for i in s:
        if i.isupper():
            kituhoa+=1
        elif i.islower():
            kituthuong+=1
    return kituhoa, kituthuong
if __name__=="__main__":
    s=input("Nhập chuỗi: ")
    print(question_3(s))