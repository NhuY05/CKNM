# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:55:14 2024

@author: Vivobook
"""
import random
def question_12():
    n=random.randint(1,1000)
    print( "n là: ",n)
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return  True
if __name__=="__main__":
    print(question_12())
    
    
def question_12() -> bool:
    n=random.randint(1,1000)
    print("snn:", n)
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    