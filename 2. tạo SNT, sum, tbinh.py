# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 23:05:51 2024

@author: Vivobook
Viết một hàm tạo ra n số nguyên ngẫu nhiên từ 1 đến 100. Sau đó, tính tổng và trung bình
của các số này.
Chữ ký hàm
Đầu vào
Đầu ra
Ví dụ
Ví dụ 1:
Một số nguyên n (1 ≤ n ≤ 1000).
Trả về 2 giá trị:
1. Tổng của các số nguyên ngẫu nhiên.
2. Trung bình của các số nguyên ngẫu nhiên
"""
import random
def question2(n: int) -> (int, float):
    songaunhien=[random.randint(1,100) for _ in range(n)]
    tong=sum(songaunhien)
    trungbinh = float(tong/n)
    return tong, trungbinh
if __name__=="__main__":
    n=int(input("Nhập n: "))
    while n<1 or n>1000:
        n=int(input("Nhập lại: "))
        
    print(question2(n))
import random    
def question_2(n: int) -> (int, float):
    songaunhien=[random.randint(1,100) for _ in range(n)]
    tong=sum(songaunhien)
    trungbinh= float(tong/n)
    return tong, trungbinh
if __name__=="__main__":
    print(question_2(5))

