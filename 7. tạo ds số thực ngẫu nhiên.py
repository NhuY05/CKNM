# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 22:23:49 2024

@author: Vivobook
"""

import random

def question_7(n: int) -> (float, float):
    danhsach=[random.uniform(0,1) for _ in range(n)]
    
    lonnhat=danhsach[0]
    nhonhat=danhsach[0]
    
    for i in danhsach:
        if i > lonnhat:
            lonnhat=i
            
        elif i < nhonhat:
            nhonhat=i
    
    return lonnhat, nhonhat
if __name__=="__main__":
    n=int(input("Nhập số lượng số: "))
    
    print(question_7(n))


