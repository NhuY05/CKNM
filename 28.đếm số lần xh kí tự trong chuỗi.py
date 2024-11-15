# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:00:12 2024

@author: Vivobook
"""
from typing import Dict
def question_28(s: str) -> Dict[str, int]:
    demkitu={}
    for kitu in s:
        if kitu in demkitu:
            demkitu[kitu]+=1
        else:
            demkitu[kitu]=1
    return demkitu
if __name__=="__main__":
    print(question_28("test"))
