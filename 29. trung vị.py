# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:09:29 2024

@author: Vivobook
"""
from typing import List
def question_29(nums: List[int]) -> float:
    nums.sort()
    n=len(nums)
    mid=n//2
    if n%2==0:
        return(nums[mid-1]+nums[mid])/2
    else:
        n%2!=0
        return nums[mid]
if __name__=="__main__":
    print(question_29([1,2,3,4,5,6,7]))