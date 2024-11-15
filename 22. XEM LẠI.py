# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:34:19 2024

@author: Vivobook
"""

def question_22(nums: list[int]) -> None:
    ds=[]
    for i in nums:
        if i!=0:
            ds.append(i)
    so0=len(nums)-len(ds)
    for i in range(so0):
        ds.append(so0)
    

















#22
def question_22(nums: list[int]) -> None:
    diachi=0
    for so in nums:
        if so !=0:
            nums[diachi]=so
            diachi+=1
    for i in range(diachi, len(nums)):
        nums[i]=0
if __name__=="__main__":
    nums=list(map(int,input("Nhập ds: ").split()))
    question_22(nums)
    print(nums)
    
def question_22(nums: list[int]) -> None:
    ds=[]
    for i in nums:
        if i!=0:
            ds.append(i)
    so0=len(nums)-len(ds)
    for i in range(so0):
        ds.append(0)
    return ds
if __name__=="__main__":
    print(question_22([0,3,4,0,5,0,6,0,3,0,0,9]))