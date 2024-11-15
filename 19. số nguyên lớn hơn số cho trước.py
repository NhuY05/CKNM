# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:54:41 2024

@author: Vivobook
"""

def is_greater(x: int, n: int) -> bool:
    if x > n:
        return True
    return False
if __name__=="__main__":
    x=int(input("Nhập x(số cần so sánh): "))
    n=int(input("Nhập n(số cho trước: "))
    print(is_greater(x, n))