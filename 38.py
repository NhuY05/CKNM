# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 23:01:56 2024

@author: Vivobook
"""

def question_38(n: int) -> int:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
print(question_38(3))