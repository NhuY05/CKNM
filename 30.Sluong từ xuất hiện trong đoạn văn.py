# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:51:30 2024

@author: Vivobook
"""
from typing import Dict
def question_30(paragraph: str) -> Dict[str, int]:
    words=paragraph.lower().split()
    demtu={}
    for tu in words:
        if tu in demtu:
            demtu[tu]+=1
        else:
            demtu[tu]=1
    return demtu
if __name__=="__main__":
    print(question_30("apple orange apple banana orange"))