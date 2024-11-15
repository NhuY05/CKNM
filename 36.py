# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:54:23 2024

@author: Vivobook
"""

import itertools
def question_36(nums: list[int]) -> list[list[int]]:
    return [list(i) for i in itertools.permutations(nums)]
if __name__=="__main__":
    print(question_36([1,2,3]))