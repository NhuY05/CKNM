# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:39:23 2024

@author: Vivobook
Viết một hàm để tìm phần tử x trong một danh sách lst . Nếu tìm thấy, trả về vị trí (chỉ số)
của phần tử đó, nếu không, trả về None .
Chữ ký hàm
Đầu vào
Đầu ra
Ví dụ
Ví dụ 1:
Giải thích: Phần tử 3 nằm ở vị trí chỉ số 2 trong danh sách.
Ví dụ 2:
Một danh sách lst chứa các số nguyên.
Một số nguyên x cần tìm trong danh sách.
Trả về chỉ số (vị trí) của phần tử x nếu tìm thấy trong danh sách.
Trả về None nếu không tìm thấy phần tử.
"""



        









def question_5(lst: list, x: int) -> int or None:
    if x in lst:
        return lst.index(x)
    else:
        return None
if __name__=="__main__":
    lst=[1,2,3,4,5]
    print(question_5(lst, 5))
    


    
    
