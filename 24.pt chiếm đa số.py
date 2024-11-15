# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:52:46 2024

@author: Vivobook
"""

import random    
def question_24(nums: list[int]) -> int:  
    n=int(input("Nhập độ dài ds số nguyên: "))
    nums=[random.randint(0,1) for _ in range(n)]
    print("ds: ", nums)
    dem=0
    phantuxh=None
    for i in nums:
        if dem==0:
            phantuxh=i
        elif i == phantuxh:
            dem+=1
    return phantuxh
if __name__=="__main__":
    nums=[]
   
    print(question_24(nums))