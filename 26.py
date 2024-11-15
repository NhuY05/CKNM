# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:47:18 2024

@author: Vivobook
"""

import collections
def question_26(s: str) -> int:
    dic_tu_so = collections.Counter(s)
    do_dai = 0
    co_so_le = False
    for so in dic_tu_so.values():
        do_dai += so // 2 * 2    
        if so % 2 == 1:
            co_so_le = True
    if co_so_le:
        do_dai += 1
    return do_dai
print(question_26("abccccdd"))
