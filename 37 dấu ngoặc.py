# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:15:30 2024

@author: Admin
"""

def question_37(s: str) -> bool:
    ds = []
    for i in s:
        if i == "(":
            ds.append(")")
        elif i == "[":
            ds.append("]")
        elif i == "{":
            ds.append("}")
        elif not ds or ds.pop() != i:
            return False
    return True
if __name__=="__main__":
    print(question_37("{"))
    print(question_37("{}}"))
    
        