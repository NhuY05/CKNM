# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:23:39 2024

@author: Vivobook
"""

def question_23(nums: list[int]) -> bool:
    dathay=set()
    for i in nums:
        if i in dathay:
            return True
        dathay.add(i)
    return False
if __name__=="__main__":
    nums=list(map(int,input("Nhập ds: ").split()))
    print(question_23(nums))

