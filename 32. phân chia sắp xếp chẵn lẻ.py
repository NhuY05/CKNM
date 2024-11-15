# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:14:52 2024

@author: Vivobook
"""
from typing import List, Tuple
def question_32(nums: List[int]) -> Tuple[List[int], List[int]]:
    sochan=[num for num in nums if num%2==0]
    sole=[num for num in nums if num%2!=0]
    sochan.sort(reverse=True)
    sole.sort()
    return sochan, sole
if __name__=="__main__":
    print(question_32([4,1,3,2,7,8,5]))