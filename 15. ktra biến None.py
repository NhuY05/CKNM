# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 00:55:29 2024

@author: Vivobook
"""

def question_15(value) -> bool:
    if value is None:
        return True
    else:
        return False
if __name__=="__main__":
    nhap = input("Nhập giá trị: ")
    if nhap=="":
        nhap=None
    print(question_15(nhap))
    


    
