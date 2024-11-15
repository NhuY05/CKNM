# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:50:55 2024

@author: Vivobook
"""

def question_34(s: str) -> int:
    danh_sach = []
    do_dai_max = 0
    for i in s:
        while i in danh_sach:
            danh_sach.pop(0)
        danh_sach.append(i)
        do_dai_max = max(do_dai_max, len(danh_sach))
    return do_dai_max
if __name__=="__main__":
    print(question_34("abcabcbb"))