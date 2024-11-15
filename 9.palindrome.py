# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:27:56 2024

@author: Vivobook
"""

def question_9(s: str) -> bool:
    s=re.sub("[^a-zA-Z]","".s.lower())
    if s==s[::-1]:
        return True
    elif s!=[::-1]:
        return False













    
import re
def question_9(s):
    s=re.sub("[^a-zA-Z]","",s.lower())
    if s !=s[::-1]:
        return False
    elif s == s[::-1]:
        return True
if __name__=="__main__":
    s=input("Nhập chuỗi: ")
    print(question_9(s))