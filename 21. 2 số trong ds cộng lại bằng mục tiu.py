# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:46:06 2024

@author: Vivobook
"""
from typing import Optional
def question_21(nums: list[int], target: int) -> Optional[tuple[int, int]]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return nums[i], nums[j]
if __name__=="__main__":
#tự nhập
    nums=list(map(int,input("nhập ds: ").split()))
    target=int(input("nhập target: "))
    print(question_21(nums, target))
#nhập sẵn    
    print(question_21([1,2,3,4,5], 9))
    
   