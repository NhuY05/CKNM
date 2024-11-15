# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 01:07:18 2024

@author: Vivobook
"""


def question_16(arg) -> float:
    if len(arg)==0:
        return None
    else:
        tong=sum(arg)
        tbc=tong/len(arg)
        return tbc
if __name__=="__main__":
    arg=list(map(int,input("Nhập: ").split()))
    print(question_16(arg))





def question_16(*args) -> float:
    if len(args) == 0:
        return None
    else:
        tong = sum(args)
        tbc = tong / len(args)
        return  tbc
if __name__ == "__main__":
    args=(list(map(int, input("Nhập: ").split())))
    
    
        
    print(question_16(*args))    
    
