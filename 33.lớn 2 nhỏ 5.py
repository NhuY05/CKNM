# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:41:02 2024

@author: Vivobook
"""

def question_33(nums: list[int]) -> tuple[int, int]:
    sokhongtrung=list(set(nums))
    sokhongtrung.sort()
    ptlonthu2=sokhongtrung[-2]if len(nums) >=2 else None
    ptnhothu5=sokhongtrung[4] if len(nums) >=5 else None
    return ptlonthu2, ptnhothu5
if __name__=="__main__":
    print(question_33([3, 1, 4, 5, 9, 2, 6, 8, 7]))