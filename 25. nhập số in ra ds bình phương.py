# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:09:11 2024

@author: Vivobook
"""

   
def question_25(nums: list[int]) -> list[int]:
    nums=list(map(int,input("Nhập ds: ").split()))
    
    binhphuong= [x ** 2 for x in nums]
    binhphuong.sort()
    return binhphuong
if __name__=="__main__":
    nums=[]
    print(question_25(nums))  