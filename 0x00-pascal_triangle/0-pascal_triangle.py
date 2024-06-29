#!/usr/bin/python3
'''
Pascal triangle module
'''

def pascal_triangle(n):
    '''Pascal triangle function'''
    li = []
    if n <= 0:
        return li
    temp_li = [1]
    li.append(temp_li)
    for i in range(1, n):
        append_li = []
        append_li.append(1)
        for j in range(1, i):
            append_li.append(temp_li[j - 1] + temp_li[j])
        append_li.append(1)
        temp_li = append_li
        li.append(append_li)
    return li
