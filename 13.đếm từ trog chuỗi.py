# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 00:36:19 2024

@author: Vivobook
"""

def question_13(s):
    tach=s.split()
    return len(tach)
if __name__=="__main__":
    s=input("Chuỗi: ")
    
    print(question_13(s))
    
def question_13(s: str) -> int:
    tach=s.split()
    return len(tach)

