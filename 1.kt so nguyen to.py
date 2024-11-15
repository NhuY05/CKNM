# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:43:39 2024

@author: Vivobook
Bạn được cung cấp một số nguyên dương n . Viết một hàm để xác định xem n có phải là
số nguyên tố hay không.
Số nguyên tố là số nguyên dương lớn hơn 1 và chỉ có hai ước số dương là 1 và chính nó.
Chữ ký hàm
Đầu vào
Đầu ra
Một số nguyên n (1 ≤ n ≤ 10^9).
Trả về True nếu n là số nguyên tố, ngược lại trả về False .
"""



def question_1(n: int) -> bool:
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
if __name__=="__main__":
    print(question_1(11))











def question1(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
if __name__=="__main__":
    n=int(input("Nhập số nguyên dương: "))
    while n <=0:
        n=int(input("Nhập lại n(phải lớn hơn 0): "))
    if question1(n):
        print("True")
    else:
        print("Hem phải số nguyên tố")
        
def question_1(n: int) -> bool:
    if n<2:
        return False
    for i in range(2,n**0.5+1):
        if n%i==0:
            return False
    return True
if __name__=="__main__":
    print(question1(11))