# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:43:55 2024

@author: Vivobook
"""

def question_27(strs: list[str]) -> str:
    if not strs:
        return ""
    tiento=strs[0]
    for chuoi in strs[1:]:
        while not chuoi.startswith(tiento):
            tiento=tiento[:-1]
            if tiento=="":
                return ""
    return tiento
if __name__=="__main__":
    print(question_27(["flower", "flow", "flight"]))
    
    
    